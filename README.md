# Akshatha — yoga

A quiet website for Akshatha, a yoga teacher from India, living in the United Kingdom.

The words and the machinery are Python, so the site is easy to change.
The pages people see are HTML, and the look is CSS. Python puts those together.

The first version is honest about what it knows. It uses your name, India, and the UK.
It does not invent a certificate, a price, a timetable, or a review.
Those can be added when you want them written down.

## See it on this computer

```bash
cd ~/Downloads/akshatha-yoga
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5050](http://127.0.0.1:5050).

On Windows, the middle two commands are:

```bash
py -m venv .venv
.venv\Scripts\activate
```

## Change the words

Open `content.py`. That file holds the sentences.
Save it, and refresh the browser.

Then rebuild the folder GitHub will host:

```bash
python build.py
```

`build.py` writes the finished site into `docs/`.
Edit `content.py`, not the files inside `docs/`. The next build replaces `docs/`.

Useful fields at the top of `content.py`:

| Field | What it does |
| --- | --- |
| `city` | Shows a city next to the United Kingdom. Leave it blank until you choose. |
| `email` | Turns the Write page into a letter that opens in the visitor's email app. |
| `instagram` | Adds the link. Write the name without `@`. |
| `SESSIONS` | The three ways to meet. Copy a block to add one. Delete a block to remove one. |

## How the files fit

```text
content.py          every sentence
app.py              the preview on your computer
build.py            makes the docs/ folder
templates/          the shape of each page
static/css/         the colours, the type, the spacing
static/js/site.js   the menu, and the letter button
static/fonts/       Newsreader and Outfit, with their licences
docs/               the finished site, created by build.py
```

## Put it on the internet for free

GitHub Pages hosts the `docs/` folder at no cost.
The repository needs to be **public**. A private repository uses a paid GitHub feature.

This project was prepared on a computer signed in to a different GitHub account,
so the repository was not created on github.com for you.
Sign in as [AkshathaAkshatha](https://github.com/AkshathaAkshatha), then:

```bash
cd ~/Downloads/akshatha-yoga
git init -b main
git add .
git commit -m "Begin the yoga website."
gh auth login
gh repo create akshatha-yoga --public --source=. --remote=origin
git push -u origin main
```

On GitHub, open the new repository, then **Settings → Pages**.
Set the source to the `main` branch and the folder `/docs`. Save.

The site will appear at:

https://akshathaakshatha.github.io/akshatha-yoga/

The first publish can take a minute. After later changes, run `python build.py`,
commit, and push. GitHub updates the live site from `docs/`.

If the repository name is not `akshatha-yoga`, change `public_url` in `content.py`
and run `python build.py` again.

## When you buy a domain

GitHub Pages can use a domain you own, still at no hosting cost.
The domain itself is the part that costs money, paid to a registrar, not to GitHub.

1. Add a file called `CNAME` inside `docs/`, containing only the domain, for example `www.yourdomain.com`.
2. In the repository, open **Settings → Pages** and enter that domain.
3. At the registrar, point the domain at GitHub using the steps here:
   [GitHub's custom domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

`build.py` keeps an existing `docs/CNAME` when it rebuilds, so the domain setting survives.

## Before the first class

Teachers who meet students in person in the UK usually arrange insurance first.
A hired room may ask to see it. The website does not say you are insured.

Add a training or a certificate to `content.py` when you want that sentence on the About page.
Until then, the page stays with the things that are already true.

## Type

Newsreader and Outfit are included under the SIL Open Font License.
The licence files are in `static/fonts/`.
