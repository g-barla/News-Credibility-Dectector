import streamlit as st
from src.analyzers import analyze_article
from src.loaders import load_from_url

st.set_page_config(page_title="News Credibility Detector", layout="wide")
st.title("📰 News Credibility Detector")

url = st.text_input("Article URL (optional)", "")
headline = st.text_input("Headline (optional)", "")
text = st.text_area("Article Text (paste if URL not provided)", "")

if st.button("🔍 Analyze"):
    # Try to fetch article if a URL is provided and fields are empty
    if url:
        try:
            fetched_title, fetched_text = load_from_url(url)
            if not headline and fetched_title:
                headline = fetched_title
            if not text and fetched_text:
                text = fetched_text
        except Exception as e:
            st.warning(f"Could not fetch article from URL: {e}")

    if not (headline or text):
        st.error("Please provide either a headline or article text (or a URL I can fetch).")
    else:
        result = analyze_article(headline=headline, text=text, url=url)
        st.subheader("Credibility Score:")
        st.success(result.get("scores", {}).get("credibility", 0))
        st.json(result)