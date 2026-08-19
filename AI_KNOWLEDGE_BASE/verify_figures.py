#!/usr/bin/env python3
"""
Figure-geometry and CSS-class verification for the note corpus.

Why this exists
---------------
Two classes of defect pass every text-based check and still reach the reader:

1. An SVG figure whose markup is perfectly valid but whose coordinates
   overlap — a heading drawn through a box, two labels on top of each other,
   text running past the viewBox. Tag balance, `node --check` and SVG
   well-formedness all pass on such a file.

2. A CSS class used in the markup that is defined nowhere in the stylesheet.
   The browser silently applies no styling, so a card grid collapses into
   full-width bars and a rounded progress pill renders as a bare block.

Both were live in this project before this script existed.

Method
------
Figures are measured in a real browser (headless Chromium via Playwright)
using getBBox() on each <text> element. An earlier version estimated text
width arithmetically from character counts; it produced eight false
positives and missed a genuine collision. Do not go back to estimating —
rendered geometry is the only thing that counts.

Usage
-----
    python3 AI_KNOWLEDGE_BASE/verify_figures.py [ROOT]

ROOT defaults to the repo root. Exits non-zero if any problem is found, so
it can be wired into a pre-commit check.

Requires: pip install playwright   (Chromium is already present in the
Claude Code web sandbox at /opt/pw-browsers/; elsewhere run
`playwright install chromium` once.)
"""

import glob
import os
import re
import sys

# ---------------------------------------------------------------- CSS classes


def check_css_classes(path):
    """Return a list of classes used in markup but defined nowhere in <style>."""
    s = open(path, encoding="utf-8", errors="ignore").read()
    css = " ".join(re.findall(r"<style.*?</style>", s, re.S))
    defined = set(re.findall(r"\.([A-Za-z][\w-]*)", css))

    body = re.sub(r"<style.*?</style>", "", s, flags=re.S)
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    used = set()
    for m in re.finditer(r'class="([^"]+)"', body):
        used.update(m.group(1).split())
    return sorted(used - defined)


# ------------------------------------------------------------------- figures

MEASURE_JS = """() => {
  const res = {count: 0, problems: []};
  document.querySelectorAll('svg').forEach((sv, si) => {
    res.count++;
    const vb = sv.viewBox.baseVal;
    if (!vb || !vb.width) return;
    const items = [...sv.querySelectorAll('text')].map(e => ({
      box: e.getBBox(), text: e.textContent.trim().slice(0, 40)
    }));

    // 1. text escaping the viewBox
    items.forEach(o => {
      const b = o.box;
      if (b.x < vb.x - 1)                        res.problems.push(`svg${si+1} OVERFLOW-LEFT  : "${o.text}"`);
      if (b.x + b.width  > vb.x + vb.width  + 1) res.problems.push(`svg${si+1} OVERFLOW-RIGHT : "${o.text}"`);
      if (b.y + b.height > vb.y + vb.height + 1) res.problems.push(`svg${si+1} OVERFLOW-BOTTOM: "${o.text}"`);
    });

    // 2. text drawn on top of other text
    for (let i = 0; i < items.length; i++) {
      for (let j = i + 1; j < items.length; j++) {
        const a = items[i].box, c = items[j].box;
        const ox = Math.min(a.x + a.width,  c.x + c.width ) - Math.max(a.x, c.x);
        const oy = Math.min(a.y + a.height, c.y + c.height) - Math.max(a.y, c.y);
        if (ox > 1 && oy > 1)
          res.problems.push(`svg${si+1} COLLIDE: "${items[i].text}" x "${items[j].text}"`);
      }
    }
  });
  return res;
}"""


def find_chromium():
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium/chrome-linux/chrome"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None  # let Playwright use its own default


def main(root):
    files = sorted(glob.glob(os.path.join(root, "**", "*.html"), recursive=True))
    if not files:
        print("no HTML files found under", root)
        return 0

    from playwright.sync_api import sync_playwright

    exe = find_chromium()
    total_figs = 0
    bad_files = 0

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            executable_path=exe, args=["--no-sandbox"]
        ) if exe else pw.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1100, "height": 900})

        for f in files:
            problems = []

            missing = check_css_classes(f)
            if missing:
                problems.append("UNDEFINED CSS CLASSES: " + ", ".join(missing))

            # Wait for DOM only, not "load": the notes link Google Fonts, and on a
            # machine without network (or behind a proxy that blocks it) the load
            # event never fires and every page would time out.
            page.goto("file://" + os.path.abspath(f),
                      wait_until="domcontentloaded", timeout=20000)
            # Give webfonts a bounded chance to arrive — text metrics depend on the
            # actual face, so measuring mid-swap would report phantom collisions.
            page.evaluate(
                "() => Promise.race(["
                "  document.fonts ? document.fonts.ready : Promise.resolve(),"
                "  new Promise(r => setTimeout(r, 2500))])"
            )
            # notes hide sections behind tabs; reveal all so every figure lays out
            page.evaluate(
                "document.querySelectorAll('.tabsection')"
                ".forEach(s => s.classList.add('active'));"
            )
            page.wait_for_timeout(150)

            result = page.evaluate(MEASURE_JS)
            total_figs += result["count"]
            problems.extend(sorted(set(result["problems"])))

            if problems:
                bad_files += 1
                print("\n" + os.path.relpath(f, root))
                for p in problems:
                    print("   ! " + p)

        browser.close()

    print("\n" + "=" * 62)
    print(f"files checked   : {len(files)}")
    print(f"figures measured: {total_figs}")
    print(f"files with problems: {bad_files}")
    return 1 if bad_files else 0


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), ".."
    )
    sys.exit(main(os.path.abspath(root)))
