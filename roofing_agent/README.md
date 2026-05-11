# 🏠 Roofing AI Agent

An **Agentic AI Chatbot** that answers roofing questions by scraping and synthesizing content from **FeedSpot's Top 100 Roofing Blogs 2026**.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Gemini API Key
Get your free API key from: https://aistudio.google.com/app/apikey

**Windows (CMD):**
```cmd
set GEMINI_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
```

**Mac/Linux:**
```bash
export GEMINI_API_KEY=your_api_key_here
```

### 3. Run the App
```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 🧠 How It Works (Agentic Architecture)

```
User Question
      ↓
[Step 1] Blog Selection
   • Scores all 40 roofing blogs by keyword relevance
   • Selects top 6 most relevant sources

      ↓
[Step 2] Web Scraping (BeautifulSoup)
   • Visits each selected blog URL
   • Extracts clean text content
   • Removes nav, footer, scripts

      ↓
[Step 3] AI Synthesis (Claude Sonnet)
   • Passes scraped content as context
   • Claude answers using ONLY those sources
   • Returns structured answer with citations

      ↓
Answer + Sources Displayed in Chat
```

---

## 📚 Source Blogs
All 40+ roofing blogs are from **FeedSpot's Top 100 Roofing Blogs 2026**:
- GAF Roofing Blog
- Owens Corning
- IKO Roofing
- Roofing Contractor Magazine
- This Old House – Roofing
- Bob Vila – Roofing
- Forbes Home Roofing
- Metal Roofing Alliance
- NRCA Blog
- ... and 30+ more

---

## 💡 Example Questions
- "What is the best roofing material for hot climates?"
- "How much does a roof replacement cost in 2026?"
- "Metal roof vs asphalt shingles — which is better?"
- "How do I fix a roof leak myself?"
- "What are signs I need a new roof?"
- "How long does an asphalt shingle roof last?"

---

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| UI | Streamlit |
| Web Scraping | BeautifulSoup4 + Requests |
| AI Model | Gemini 2.5 Flash (Google) |
| Agentic Loop | Custom Python |

---

## 📁 File Structure
```
roofing_agent/
├── app.py           ← Main Streamlit application
├── requirements.txt ← Python dependencies
└── README.md        ← This file
```
