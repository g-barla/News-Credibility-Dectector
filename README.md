# 📰 AI News Credibility & Misinformation Detector

An **AI-powered tool** that analyzes news articles for credibility, consistency, and sensationalism.  
Paste a URL or article text → get an explainable credibility score with signals like headline–body consistency, clickbait patterns, and framing.

---

## 🚀 Features
- 📰 **Headline–Body Consistency (NLI)** — checks if the headline is supported by the article body  
- 🔎 **Clickbait & Sensationalism Detection** — regex + style heuristics  
- 📊 **Credibility Score (0–100)** — transparent, weighted blend of signals  
- 🛠️ **Explainability** — shows the raw model evidence and which NLI model is used  
- ⚡ **Fast Demo** — Streamlit UI, no training required  

---

## 📷 Screenshots
- Main App: `assets/App.screenshot.png`
- Results: `assets/Reportscreenshot1.png`  

---

## 🛠️ Tech Stack
- **UI:** Streamlit  
- **NLP:** Hugging Face Transformers (zero-shot NLI)  
- **Parsing:** newspaper3k, tldextract  
- **Heuristics:** regex rules for clickbait/sensationalism  

---

## ⚡ Quickstart

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
