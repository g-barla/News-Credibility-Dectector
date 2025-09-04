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

<img width="1403" height="532" alt="App screenshot" src="https://github.com/user-attachments/assets/126f5b1c-d24e-476b-b956-820c8fedfee7" />
<img width="1422" height="462" alt="Reportscreenshot1" src="https://github.com/user-attachments/assets/7c6715e5-32bb-420c-a2d3-c657bcdb6c46" />
<img width="1386" height="684" alt="Screenshot 2025-09-04 at 1 27 05 PM" src="https://github.com/user-attachments/assets/6c04278f-761a-41d7-a444-cd97dae701e7" />

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
