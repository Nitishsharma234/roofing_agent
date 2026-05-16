# 🏠 Roofing AI Agent

A smart chatbot that answers roofing questions by reading real roofing websites and using AI to give you a proper answer.

---

## What We Used

| Tool | What it does |
|------|-------------|
| **Streamlit** | Builds the chat interface you see in the browser |
| **Groq API** | Runs the AI brain (LLaMA 3.3 70B model) — fast and free |
| **BeautifulSoup** | Reads and extracts text from roofing websites |
| **Requests** | Fetches the web pages from the internet |
| **Python** | The language everything is written in |

---

## How It Works (Step by Step)

1. **You type a question** — like *"How much does a metal roof cost?"*

2. **Small-talk check** — if you just say "hi" or "thanks", the bot replies casually without wasting any API calls.

3. **Pick the best sources** — the app picks the 8 most relevant roofing blogs from a list of 40 top sources.

4. **Scrape the websites** — it visits those websites and grabs the text content (up to 3000 characters each).

5. **Send to AI** — the scraped text + your question are sent to Groq's LLaMA model.

6. **Get the answer** — the AI reads the content and writes a clear, structured answer for you.

7. **Show sources** — the websites that were used are shown as clickable links below the answer.

---

## File Structure

```
app.py       → Main app — handles the chat UI and ties everything together
scraper.py   → Fetches web pages and calls the Groq AI
styles.py    → All the CSS styling (dark theme, colors, fonts)
```

---

## How to Run

```bash
# Install dependencies
pip install streamlit groq requests beautifulsoup4

# Set your Groq API key
export GROQ_API_KEY=your_key_here

# Run the app
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## Key Features

- 💬 Chat-style interface with message history
- 🔍 Searches 40+ real roofing blogs live
- 🤖 Powered by LLaMA 3.3 70B via Groq
- 🚫 Smart filter to skip non-roofing / small-talk messages
- 📚 Shows clickable source links for every answer
- 🎨 Clean dark UI with sidebar example questions
