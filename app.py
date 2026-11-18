"""Preview the website on this computer.

    python app.py

Then open http://127.0.0.1:5050

GitHub does not run this file. GitHub hosts the finished pages
that build.py writes into the docs/ folder.
"""

from flask import Flask, render_template

from content import PAGES, build_context, validate

validate()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

PAGE_BY_KEY = {page["key"]: page for page in PAGES}


def render_page(key: str):
    page = PAGE_BY_KEY[key]
    return render_template(page["template"], **build_context(key))


@app.get("/")
@app.get("/index.html")
def home():
    return render_page("home")


@app.get("/<key>.html")
def inner(key: str):
    if key not in PAGE_BY_KEY or key == "home":
        return missing(None)
    return render_page(key)


@app.errorhandler(404)
def missing(_error):
    html = render_template("404.html", **build_context("missing"))
    return html, 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5050)
