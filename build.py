"""Write the website into the docs/ folder.

    python build.py

GitHub Pages can host that folder for free.
It serves the HTML as it is. It does not run the Python.
"""

from pathlib import Path
import re
import shutil

from flask import render_template

from app import app
from content import PAGES, SITE, build_context

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
STATIC = ROOT / "static"

BUILT_PAGES = list(PAGES) + [
    {"key": "missing", "file": "404.html", "template": "404.html"},
]


def render(key: str, template: str) -> str:
    with app.test_request_context("/"):
        return render_template(template, **build_context(key))


def write_pages() -> list[Path]:
    written = []
    for page in BUILT_PAGES:
        html = render(page["key"], page["template"])
        path = DOCS / page["file"]
        path.write_text(html, encoding="utf-8")
        written.append(path)
    return written


def write_extras() -> None:
    base = SITE["public_url"].rstrip("/")
    addresses = [f"{base}/"]
    for page in PAGES:
        if page["key"] == "home":
            continue
        addresses.append(f"{base}/{page['file']}")

    urls = "".join(f"  <url><loc>{address}</loc></url>\n" for address in addresses)
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}"
        "</urlset>\n"
    )
    (DOCS / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (DOCS / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n" f"Sitemap: {base}/sitemap.xml\n",
        encoding="utf-8",
    )
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")


def check_links(files: list[Path]) -> None:
    pattern = re.compile(r'(?:href|src)="([^"]+)"')
    for path in files:
        text = path.read_text(encoding="utf-8")
        for match in pattern.findall(text):
            if match.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = match.split("#", 1)[0].split("?", 1)[0]
            if target and not (path.parent / target).exists():
                raise SystemExit(f"{path.name} points to a missing file: {target}")

    css_path = DOCS / "static" / "css" / "style.css"
    css = css_path.read_text(encoding="utf-8")
    for match in re.findall(r'url\("([^"]+)"\)', css):
        font = (css_path.parent / match).resolve()
        if not font.exists():
            raise SystemExit(f"The stylesheet points to a missing file: {match}")


def main() -> None:
    cname = DOCS / "CNAME"
    preserved = cname.read_text(encoding="utf-8") if cname.exists() else None

    if DOCS.exists():
        shutil.rmtree(DOCS)

    shutil.copytree(STATIC, DOCS / "static")
    files = write_pages()
    write_extras()

    if preserved is not None:
        (DOCS / "CNAME").write_text(preserved, encoding="utf-8")

    check_links(files)
    print(f"Built {len(files)} pages in {DOCS}")


if __name__ == "__main__":
    main()
