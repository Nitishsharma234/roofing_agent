# scraper.py
import os
import re
import requests
from bs4 import BeautifulSoup
from groq import Groq

# ─────────────────────────────────────────────
#  GROQ CLIENT  — set GROQ_API_KEY in your env
# ─────────────────────────────────────────────
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "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")

ROOFING_BLOGS = [
    {"name": "GAF Roofing Blog",               "url": "https://www.gaf.com/en-us/blog"},
    {"name": "Owens Corning Roofing",          "url": "https://www.owenscorning.com/en-us/roofing/blog"},
    {"name": "CertainTeed Roofing",            "url": "https://www.certainteed.com/roofing/resources/"},
    {"name": "IKO Roofing Blog",               "url": "https://www.iko.com/na/blog/"},
    {"name": "Metal Roofing Alliance",         "url": "https://www.metalroofing.com/blog/"},
    {"name": "NRCA – National Roofing",        "url": "https://www.nrca.net/news"},
    {"name": "Roofing Contractor Magazine",    "url": "https://www.roofingcontractor.com/"},
    {"name": "Roofing Today",                  "url": "https://roofingtoday.com/blog/"},
    {"name": "Roof Online",                    "url": "https://roofonline.com/blog/"},
    {"name": "The Roofing Blog",               "url": "https://theroofingblog.com/"},
    {"name": "Angi – Roofing Articles",        "url": "https://www.angi.com/articles/roofing/"},
    {"name": "Bob Vila – Roofing",             "url": "https://www.bobvila.com/sections/roofing/"},
    {"name": "This Old House – Roofing",       "url": "https://www.thisoldhouse.com/roofing"},
    {"name": "Family Handyman Roofing",        "url": "https://www.familyhandyman.com/list/roofing-advice-and-tips/"},
    {"name": "HomeAdvisor Roofing",            "url": "https://www.homeadvisor.com/r/roofing/"},
    {"name": "Modernize Roofing Blog",         "url": "https://modernize.com/roofing"},
    {"name": "Forbes Home – Roofing",          "url": "https://www.forbes.com/home-improvement/roofing/"},
    {"name": "Fixr Roofing Guide",             "url": "https://www.fixr.com/costs/roof-installation"},
    {"name": "RoofCalc.org",                   "url": "https://roofcalc.org/blog/"},
    {"name": "Architectural Digest Roofing",   "url": "https://www.architecturaldigest.com/home-improvement/roof"},
    {"name": "Roof Advisor",                   "url": "https://www.roofadvisor.com/blog/"},
    {"name": "RoofingMegaStore Blog",          "url": "https://www.roofingmegastore.co.uk/blog/"},
    {"name": "DIY Network – Roofing",          "url": "https://www.diynetwork.com/how-to/rooms-and-spaces/outdoor/roofing"},
    {"name": "HomeGuide Roofing",              "url": "https://homeguide.com/costs/roofing-cost"},
    {"name": "Thumbtack Roofing",              "url": "https://www.thumbtack.com/p/roofing-cost"},
    {"name": "Porch Roofing Blog",             "url": "https://porch.com/advice/roofing"},
    {"name": "Roof Hub",                       "url": "https://roofhub.com/blog/"},
    {"name": "SRS Distribution Blog",          "url": "https://www.srsdistribution.com/blog/"},
    {"name": "ABC Supply Blog",                "url": "https://www.abcsupply.com/blog/"},
    {"name": "Metal Roof Network",             "url": "https://metalroofnetwork.com/blog/"},
    {"name": "Green Building Advisor – Roof",  "url": "https://www.greenbuildingadvisor.com/topic/roofing"},
    {"name": "Energy.gov – Roof & Attic",      "url": "https://www.energy.gov/energysaver/energy-efficient-roofing"},
    {"name": "ENERGY STAR Roofing",            "url": "https://www.energystar.gov/products/building_products/roof_products"},
    {"name": "Cool Roof Rating Council",       "url": "https://coolroofs.org/resources/"},
    {"name": "Roofing World Blog",             "url": "https://roofingworldmag.com/"},
    {"name": "Roofle Blog",                    "url": "https://roofle.com/blog/"},
    {"name": "ImproveNet Roofing",             "url": "https://www.improvenet.com/r/costs-and-prices/roofing"},
    {"name": "Zillow Roofing Tips",            "url": "https://www.zillow.com/learn/roof-replacement-cost/"},
    {"name": "Remodeling Costs Roofing",       "url": "https://www.remodelingcosts.org/roof-replacement-cost/"},
    {"name": "Sears Roofing Blog",             "url": "https://www.searshomeservices.com/blog/roofing/"},
]

# ─────────────────────────────────────────────
#  ROOFING KEYWORDS — used to decide if input is a real question
# ─────────────────────────────────────────────
_ROOFING_KEYWORDS = {
    "roof", "roofing", "shingle", "shingles", "leak", "leaking", "repair", "replace",
    "replacement", "metal", "tile", "flat", "cost", "price", "estimate", "material",
    "materials", "install", "installation", "damage", "gutter", "flashing", "underlayment",
    "asphalt", "slate", "wood", "composite", "ventilation", "attic", "insulation",
    "contractor", "inspection", "warranty", "lifespan", "waterproof", "pitch", "slope",
}

# ─────────────────────────────────────────────
#  SMALL-TALK DETECTOR
# ─────────────────────────────────────────────
_GREETINGS = {
    "hi", "hey", "hello", "howdy", "yo", "sup", "hiya", "heya",
    "whats up", "what's up", "hi there", "hey there",
    "good morning", "good afternoon", "good evening", "good night",
    "how are you", "how r u", "how's it going", "how do you do",
}
_THANKS = {"thanks", "thank you", "thx", "ty", "cheers"}
_BYES   = {"bye", "goodbye", "see you", "see ya", "cya", "take care"}
_OKS    = {"ok", "okay", "cool", "great", "awesome", "nice", "lol", "haha", "k", "got it"}
_WHO    = {"who are you", "what are you", "what can you do", "what do you do"}
_HELP   = {"help"}


def _clean(text: str) -> str:
    """Lowercase, strip trailing punctuation, collapse repeated chars (hiii → hi)."""
    text = text.strip().lower()
    text = re.sub(r"[!?.,]+$", "", text).strip()
    text = re.sub(r"(.)\1{2,}", r"\1", text)   # hiii→hi, heyyyy→hey
    return text


def _is_roofing_question(text: str) -> bool:
    """Returns True only if the text contains at least one roofing keyword."""
    words = set(re.sub(r"[^a-z0-9 ]", "", text.lower()).split())
    return bool(words & _ROOFING_KEYWORDS)


def detect_small_talk(text: str):
    """Returns a reply string for small talk, or None if it's a real roofing question."""
    c = _clean(text)

    # Exact set matches
    if c in _GREETINGS:
        return "Hey! 👋 What roofing question can I help you with?"
    if c in _THANKS:
        return "No problem! Let me know if you have more questions. 🏠"
    if c in _BYES:
        return "Take care! Come back anytime for roofing help. 👋"
    if c in _OKS:
        return "Sure! Ask me anything about roofing. 🏠"
    if c in _WHO:
        return (
            "I'm your Roofing AI Agent — I search the top roofing blogs to answer your questions. "
            "Try asking something like *'How much does a metal roof cost?'*"
        )
    if c in _HELP:
        return (
            "Just type any roofing question! For example:\n"
            "- How much does a roof replacement cost?\n"
            "- What's the best roofing material?\n"
            "- How do I fix a roof leak?"
        )

    # Starts-with greeting check (catches "hello there", "hey how are you" etc.)
    greeting_words = ("hi", "hey", "hello", "howdy", "hiya", "heya", "yo")
    if any(c == g or c.startswith(g + " ") for g in greeting_words):
        return "Hey! 👋 What roofing question can I help you with?"

    # Short input with no roofing keywords → don't send to Groq
    if len(c.split()) <= 4 and not _is_roofing_question(text):
        return "Hey! 👋 Ask me anything about roofing — materials, costs, repairs, you name it."

    return None  # real roofing question → run full agent


# ─────────────────────────────────────────────
#  SCRAPING
# ─────────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


def scrape_page(url: str, max_chars: int = 3000) -> str:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header",
                          "aside", "form", "iframe", "noscript"]):
            tag.decompose()
        text = re.sub(r"\s+", " ", soup.get_text(separator=" ", strip=True))
        return text[:max_chars]
    except Exception as e:
        return f"[Could not fetch: {e}]"


def find_relevant_blogs(query: str, blogs: list, top_n: int = 8) -> list:
    query_words = set(re.sub(r"[^a-z0-9 ]", "", query.lower()).split())
    scored = [(sum(1 for w in query_words if w in (b["name"] + b["url"]).lower()), b)
              for b in blogs]
    scored.sort(key=lambda x: -x[0])
    return [b for _, b in scored[:top_n]]


# ─────────────────────────────────────────────
#  MAIN AGENT
# ─────────────────────────────────────────────
def run_agent(query: str, status_container) -> dict:
    # Short-circuit for small talk — no scraping, no API call
    casual = detect_small_talk(query)
    if casual:
        return {"answer": casual, "sources": []}

    if not GROQ_API_KEY:
        return {
            "answer": "⚠️ Groq API key is not set. Please set the `GROQ_API_KEY` environment variable.",
            "sources": [],
        }

    client = Groq(api_key=GROQ_API_KEY)

    status_container.markdown(
        '<span class="status-badge badge-search">🔍 Selecting roofing sources…</span>',
        unsafe_allow_html=True,
    )
    selected_blogs = find_relevant_blogs(query, ROOFING_BLOGS, top_n=8)

    scraped_data = []
    for blog in selected_blogs:
        status_container.markdown(
            f'<span class="status-badge badge-reading">📖 Reading: {blog["name"]}</span>',
            unsafe_allow_html=True,
        )
        content = scrape_page(blog["url"])
        if not content.startswith("[Could not fetch"):
            scraped_data.append({"name": blog["name"], "url": blog["url"], "content": content})
        if len(scraped_data) >= 4:
            break

    status_container.markdown(
        '<span class="status-badge badge-thinking">🧠 Groq LLaMA 3.3 70B thinking…</span>',
        unsafe_allow_html=True,
    )

    if scraped_data:
        context_blocks = "\n\n".join(
            f"=== SOURCE: {d['name']} ({d['url']}) ===\n{d['content']}"
            for d in scraped_data
        )
        source_instruction = "Answer using the source content below, citing which sources you used."
    else:
        context_blocks = "(No sources could be scraped. Use your expert roofing knowledge.)"
        source_instruction = (
            "The web sources could not be fetched. Answer from your expert roofing knowledge "
            "and note that the answer is from general knowledge."
        )

    prompt = f"Question: {query}\n\n{source_instruction}\n\nSource Content:\n{context_blocks}"

    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a friendly, knowledgeable AI roofing expert. "
                    "Talk like a real human — simple, clear, never robotic. "
                    "Always structure your answers in this exact format:\n\n"
                    "1. Start with 1–2 sentences giving a direct, helpful intro to the topic.\n\n"
                    "2. Then include two clearly labeled sections using bold headers, each with bullet points:\n"
                    "   - A 'When [X] may be enough' section (e.g. 'When a repair may be enough')\n"
                    "   - A 'When [Y] is usually recommended' section (e.g. 'When replacement is usually recommended')\n"
                    "   Each bullet should be bolded with a short label, followed by a dash and a 1–2 sentence explanation.\n\n"
                    "3. End with a 'Next steps you can take' section: a numbered list of 3 actionable steps.\n\n"
                    "4. Close with 1–2 sentences inviting the user to share more details for a tailored answer.\n\n"
                    "Always follow this structure regardless of the question. Adapt the section headers to fit the topic. "
                    "If the user's question is very short or casual (under 5 words), keep your answer short and conversational — skip the structured format."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=1500,
    )

    answer = chat.choices[0].message.content
    sources_used = [{"name": d["name"], "url": d["url"]} for d in scraped_data]
    return {"answer": answer, "sources": sources_used}
