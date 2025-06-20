# src/analyzers.py
from transformers import pipeline
from .heuristics import detect_clickbait

# lazy global so model loads once
_NLI = None
def _get_nli():
    global _NLI
    if _NLI is None:
        _NLI = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return _NLI

def analyze_article(headline: str = "", text: str = "", url: str = None):
    """
    Returns dict with scores + explanations.
    `url` is accepted for provenance but not required for scoring.
    """
    out = {"scores": {}, "explanations": {}}
    headline = (headline or "").strip()
    text = (text or "").strip()

    credibility = 0

    # 1) NLI support (0..100)
    nli_pct = 50
    if headline and text:
        nli = _get_nli()
        res = nli(
            headline,
            candidate_labels=[
                "supported by the article body",
                "refuted by the article body",
            ],
            hypothesis_template="This headline is {}.",
        )
        # first label corresponds to "supported"
        nli_pct = int(res["scores"][0] * 100)
        out["explanations"]["nli"] = {
            "sequence": headline,
            "labels": res["labels"],
            "scores": res["scores"],
        }

    # 2) Clickbait heuristic (0..100, higher = worse)
    cb = detect_clickbait(headline)
    out["explanations"]["clickbait"] = cb

    # 3) Combine with conservative weights:
    #    - NLI can be gamed by self-consistent fake claims,
    #      so give it 30% weight.
    #    - Anti-clickbait (100 - cb) gets 70% weight.
    credibility = 0.30 * nli_pct + 0.70 * (100 - cb)

    # clamp
    out["scores"]["credibility"] = int(max(0, min(100, round(credibility))))
    out["scores"]["nli_support"] = nli_pct
    out["scores"]["clickbait"] = cb
    return out