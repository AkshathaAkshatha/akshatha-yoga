"""The words on the website.

Edit this file when you want to change what people read.
The layouts live in templates/. The colours live in static/css/style.css.

After a change, run:

    python app.py       preview on this computer
    python build.py     refresh the docs/ folder that GitHub hosts
"""

from __future__ import annotations

import json
from datetime import date


# ---------------------------------------------------------------------------
# Your details. These appear in the header, the footer, and the page titles.
# ---------------------------------------------------------------------------

SITE = {
    "name": "Akshatha",
    "role": "Yoga",
    "from_place": "India",
    "lives_in": "United Kingdom",
    # Add a city when you want one, for example "Bristol". Leave blank for now.
    "city": "",
    # Your public email. Leave blank until you are ready to publish it.
    "email": "",
    # Instagram name, without the @. Leave blank and the link stays hidden.
    "instagram": "akshatha.yoga",
    "language": "English",
    # The free address GitHub Pages will use. Change this if you rename the repo.
    "public_url": "https://akshathaakshatha.github.io/akshatha-yoga",
    "nav": [
        {"key": "practice", "label": "Practice"},
        {"key": "sessions", "label": "Sessions"},
        {"key": "about", "label": "About"},
        {"key": "visit", "label": "Write"},
    ],
}


# ---------------------------------------------------------------------------
# Home.
# ---------------------------------------------------------------------------

HOME = {
    "document_title": "Akshatha — Yoga teacher in the United Kingdom",
    "description": (
        "Akshatha teaches yoga in the United Kingdom. "
        "Calm, precise classes for beginners and for people returning to practice."
    ),
    "kicker": "Yoga teacher",
    "title": "Practice,",
    "title_em": "without hurry.",
    "lede": (
        "I am Akshatha. I am from India, and I live in the United Kingdom. "
        "I teach yoga as a steady hour of breath, strength, and rest, "
        "shaped for the person in front of me."
    ),
    "mark_caption": "Breath  ·  Strength  ·  Rest",
    "principles_kicker": "In the room",
    "principles_title": "Three agreements.",
    "principles": [
        {
            "title": "Breath before shape",
            "text": (
                "If the breath is strained, the shape is too far. "
                "We change it. The pose is there to serve you."
            ),
        },
        {
            "title": "Strength, kept kind",
            "text": (
                "You will work. Legs, back, and attention all take part. "
                "The effort stays kind."
            ),
        },
        {
            "title": "Rest is included",
            "text": (
                "Stillness is practised in the same way standing is practised. "
                "It belongs in the hour."
            ),
        },
    ],
    "for_kicker": "Who it suits",
    "for_title": "Beginners, and people returning.",
    "for_intro": "Any age, any body. Experience is optional.",
    "for_items": [
        "You have never been to a yoga class, and you want to know what to do.",
        "You used to practise, and you want a clean way back.",
        "You already practise, and you want teaching that is specific.",
        "Your week is full, and you want one hour that is simple and complete.",
    ],
    "map_kicker": "On this site",
    "map_title": "Four short pages.",
    "map": [
        {
            "key": "practice",
            "label": "Practice",
            "text": "How a class is taught, and the order we keep.",
        },
        {
            "key": "sessions",
            "label": "Sessions",
            "text": "A private hour, a small group, or a class online.",
        },
        {
            "key": "about",
            "label": "About",
            "text": "Who I am, and the standard I teach by.",
        },
        {
            "key": "visit",
            "label": "Write",
            "text": "Tell me a little, and we will find a time.",
        },
    ],
    "close_title": "If you would like to practise together, write to me.",
    "close_text": (
        "Say where you are, what your body needs me to know, "
        "and which kind of session you want. A short note is enough. "
        "You can also follow, and write to me, on Instagram."
    ),
    "instagram_label": "Follow on Instagram",
}


# ---------------------------------------------------------------------------
# The practice.
# ---------------------------------------------------------------------------

PRACTICE = {
    "document_title": "The practice — Akshatha",
    "description": (
        "How Akshatha teaches a yoga class: breath first, "
        "a clear option beside each shape, and a rest that is long enough."
    ),
    "kicker": "Practice",
    "title": "A class with a beginning,",
    "title_em": "a middle, and an end.",
    "lede": (
        "You will always know which part of the hour you are in. "
        "Nothing is there to catch you out."
    ),
    "paragraphs": [
        (
            "We start on the floor or on the feet, depending on the day. "
            "The breath comes first. It is a count you can return to "
            "when a shape asks for effort."
        ),
        (
            "I name the feeling I want, and the part of the body that does the work. "
            "When a shape is unfamiliar, a second version sits beside it. "
            "Choosing that version is part of practising well."
        ),
        (
            "We finish still, for long enough that the hour can land. "
            "Then one plain suggestion for the week ahead. Often it is a minute "
            "of the same breath, on a day you do not come to class."
        ),
    ],
    "order_kicker": "The hour",
    "order_title": "What we do, in order.",
    "order": [
        {
            "title": "Arrive",
            "text": (
                "A few quiet minutes. You do not need to be calm already. "
                "Arriving is the first practice."
            ),
        },
        {
            "title": "Breathe",
            "text": "A simple pattern, taught out loud, until it feels familiar.",
        },
        {
            "title": "Stand and balance",
            "text": (
                "Strength for the legs and the back, with a wall or a chair "
                "when a hand makes the shape steadier."
            ),
        },
        {
            "title": "Go to the floor",
            "text": "Hips, back, and belly. Slower here. Room for questions.",
        },
        {
            "title": "Rest",
            "text": "Lying down, covered if you wish, with nothing else to do.",
        },
        {
            "title": "Leave with one thing",
            "text": "A single practice small enough to repeat at home.",
        },
    ],
    "boundary_title": "A clear boundary",
    "boundary": (
        "I do not force a shape. I do not promise that yoga will heal an injury. "
        "If something hurts in a sharp way, we stop and we change it. "
        "A doctor, a midwife, or a physiotherapist comes before a class."
    ),
}


# ---------------------------------------------------------------------------
# Sessions. Copy a block to add another way of meeting.
# Delete a block to remove one.
# ---------------------------------------------------------------------------

SESSIONS = [
    {
        "name": "Private",
        "time": "About one hour",
        "where": "A quiet room, or online",
        "summary": (
            "One student. The hour follows your body, your questions, "
            "and the week you are actually having."
        ),
        "points": [
            "A good fit when you are beginning, returning, or working around an injury.",
            "We agree the aim before we start.",
            "You leave with a short practice you can repeat alone.",
        ],
    },
    {
        "name": "Small group",
        "time": "About one hour",
        "where": "In person",
        "summary": (
            "A few people, and one shared rhythm. Enough company to feel a class. "
            "Few enough that the teaching can stay personal."
        ),
        "points": [
            "The same sequence for everyone, with a gentler option beside the stronger shapes.",
            "Questions are welcome while we practise.",
            "You can take part without being flexible.",
        ],
    },
    {
        "name": "Online",
        "time": "About one hour",
        "where": "Your floor, and a screen",
        "summary": (
            "For weeks when the room is too far. Set a phone or a laptop "
            "at the side of the mat, so the teaching can still see you."
        ),
        "points": [
            "A clear bit of floor is enough.",
            "The plan is simple enough to survive a poor connection.",
            "If you cannot hear, we pause.",
        ],
    },
]

SESSION_PAGE = {
    "document_title": "Sessions — Akshatha",
    "description": (
        "Private yoga, small groups, and online classes with Akshatha, "
        "taught from the United Kingdom."
    ),
    "kicker": "Sessions",
    "title": "Three ways",
    "title_em": "to meet.",
    "lede": "Choose the form that fits the week. The teaching stays the same.",
    "shared_kicker": "Before we meet",
    "shared_title": "Practical things.",
}

SHARED = [
    {
        "title": "What to bring",
        "text": (
            "Clothes you can sit, stand, and lie down in. A mat, if you have one. "
            "When we meet in a room I prepare, a mat will be there. "
            "Water is useful. Eat lightly beforehand if you can."
        ),
    },
    {
        "title": "The fee",
        "text": (
            "I tell you the fee before you book. "
            "The hour does not end with a surprise."
        ),
    },
    {
        "title": "Changing an hour",
        "text": (
            "Send a note as soon as you know you need a different time. "
            "We will find another one."
        ),
    },
    {
        "title": "Injury, pregnancy, and illness",
        "text": (
            "Tell me before we meet. I will change the class around what you tell me. "
            "I do not replace a doctor, a midwife, or a physiotherapist."
        ),
    },
]


# ---------------------------------------------------------------------------
# About.
# ---------------------------------------------------------------------------

ABOUT = {
    "document_title": "About Akshatha",
    "description": "Akshatha is a yoga teacher from India, living in the United Kingdom.",
    "kicker": "About",
    "title": "From India.",
    "title_em": "Teaching in the United\u00a0Kingdom.",
    "lede": "The classes are in English. They are built for ordinary weeks.",
    "paragraphs": [
        (
            "My name is Akshatha. I am from India, and I live in the United Kingdom. "
            "People arrive from work, from the weather, from a small room, "
            "or from a long time away from practice. The hour has to be useful for that life."
        ),
        (
            "I would rather you leave with one thing you can repeat "
            "than with ten shapes you cannot find again on your own. "
            "Slow teaching is how the one thing sticks."
        ),
    ],
    "script": "अक्षत",
    "script_meaning": "Whole. Unbroken.",
    "script_note": (
        "The name Akshatha comes from this word. "
        "I keep it as a standard. You can begin as you are."
    ),
    "begin_kicker": "A first class",
    "begin_title": "How we start.",
    "begin": [
        {
            "title": "You write",
            "text": (
                "A short note is enough. Where you are, what I should know, "
                "and the sort of session you want."
            ),
        },
        {
            "title": "We agree",
            "text": "A time, a fee, and a place. That place may be a room, a hired hall, or a screen.",
        },
        {
            "title": "We begin smaller than you might expect",
            "text": "The first hour is for learning how you move, and how you like to be taught.",
        },
        {
            "title": "You leave with a way back in",
            "text": "One short practice, so the week after the class still belongs to you.",
        },
    ],
}


# ---------------------------------------------------------------------------
# The letter page.
# ---------------------------------------------------------------------------

VISIT = {
    "document_title": "Write to Akshatha",
    "description": "Arrange a yoga session with Akshatha. Private, small group, or online.",
    "kicker": "Write",
    "title": "A short note",
    "title_em": "is enough.",
    "lede": (
        "Tell me where you are, what your body needs me to know, "
        "and whether you want a private hour, a small group, or an online class."
    ),
    "prompts_title": "Useful things to include",
    "prompts": [
        "Whether you have practised yoga before.",
        "Any injury, pregnancy, or illness I should teach around.",
        "The days and times that are possible.",
        "Whether you would rather meet in person or online.",
    ],
    "instagram_kicker": "Instagram",
    "instagram_text": (
        "Follow the practice there. You can also send a message, "
        "and I will read it."
    ),
    "button_send": "Open the letter",
    "button_draft": "Prepare the note",
    "send_ready": "This opens a letter in your email app, addressed to me.",
    "send_later": (
        "Compose the note here, then copy it into an Instagram message. "
        "It stays on the page until you are ready to send it."
    ),
    "ready_kicker": "Your note",
    "note_placeholder": "A few lines are plenty.",
}


MISSING = {
    "document_title": "Page not found — Akshatha",
    "description": "This page is not on Akshatha's yoga site.",
    "kicker": "Missing page",
    "title": "This page",
    "title_em": "is not here.",
    "lede": "The address may be old. The rest of the site is where it was.",
}


# The builder and the local site both walk this list.
# key      the name used in Python
# file     the address on the internet
# template the layout in templates/

PAGES = [
    {"key": "home", "file": "index.html", "template": "index.html"},
    {"key": "practice", "file": "practice.html", "template": "practice.html"},
    {"key": "sessions", "file": "sessions.html", "template": "sessions.html"},
    {"key": "about", "file": "about.html", "template": "about.html"},
    {"key": "visit", "file": "visit.html", "template": "visit.html"},
]


def validate() -> None:
    """Stop early, with a plain message, if a detail is unfinished in the wrong way."""
    email = SITE["email"].strip()
    if email and "@" not in email:
        raise SystemExit(
            "The email in content.py needs a full address, or it can be left empty."
        )

    url = SITE["public_url"].strip()
    if not url.startswith("https://"):
        raise SystemExit("public_url in content.py should start with https://")

    keys = [page["key"] for page in PAGES]
    if len(keys) != len(set(keys)):
        raise SystemExit("Two pages in content.py share the same key.")

    for session in SESSIONS:
        for field in ("name", "time", "where", "summary"):
            if not str(session.get(field, "")).strip():
                raise SystemExit(f"A session in content.py is missing its {field}.")


def _location() -> str:
    city = SITE["city"].strip()
    country = SITE["lives_in"].strip()
    if city:
        return f"{city}, {country}"
    return country


def _page_meta(current: str) -> dict:
    source = {
        "home": HOME,
        "practice": PRACTICE,
        "sessions": SESSION_PAGE,
        "about": ABOUT,
        "visit": VISIT,
        "missing": MISSING,
    }[current]
    if current == "home":
        file_name = "index.html"
    elif current == "missing":
        file_name = "404.html"
    else:
        file_name = f"{current}.html"

    base = SITE["public_url"].rstrip("/")
    if current == "home":
        canonical = f"{base}/"
    else:
        canonical = f"{base}/{file_name}"

    return {
        "document_title": source["document_title"],
        "description": source["description"],
        "canonical": canonical,
        "file": file_name,
    }


def _schema(location: str, email: str, instagram_url: str) -> str:
    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": SITE["name"],
        "jobTitle": "Yoga teacher",
        "homeLocation": location,
        "url": SITE["public_url"],
        "knowsLanguage": SITE["language"],
    }
    if email:
        person["email"] = email
    if instagram_url:
        person["sameAs"] = [instagram_url]
    return json.dumps(person, ensure_ascii=False).replace("<", "\\u003c")


def build_context(current: str) -> dict:
    """Everything a page is allowed to show."""
    email = SITE["email"].strip()
    instagram = SITE["instagram"].strip().lstrip("@").strip("/")
    instagram_url = f"https://www.instagram.com/{instagram}/" if instagram else ""
    location = _location()
    choices = [session["name"] for session in SESSIONS]
    choices.append("Not sure yet")

    return {
        "site": SITE,
        "home": HOME,
        "practice": PRACTICE,
        "sessions": SESSIONS,
        "session_page": SESSION_PAGE,
        "shared": SHARED,
        "about": ABOUT,
        "visit": VISIT,
        "missing": MISSING,
        "current": current,
        "year": date.today().year,
        "location": location,
        "email": email,
        "instagram": instagram,
        "instagram_url": instagram_url,
        "session_choices": choices,
        "page_meta": _page_meta(current),
        "schema_json": _schema(location, email, instagram_url) if current == "home" else "",
    }
