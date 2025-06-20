# src/heuristics.py
import re

CLICKBAIT_WORDS = [
    r"\bbreaking\b",
    r"\bsecret\b",
    r"\byou\s+won.?t\s+believe\b",
    r"\bmiracle\b",
    r"\bcures?\s+all\b",
    r"\bshocking\b",
    r"\bstunned?\b",
    r"\bstaggering\b",
    r"\bexposed\b",
    r"\bovernight\b",
    r"\binstant(ly)?\b",
    r"\bhidden\b",
    r"\bwhat\s+happened\s+next\b",
]

def detect_clickbait(headline: str) -> int:
    """
    Heuristic clickbait score 0..100
    - keyword hits
    - excessive exclamations
    - ALL CAPS ratio
    """
    h = headline.strip()
    if not h:
        return 0

    lc = h.lower()

    # keyword hits (each adds 12, cap via 0..100)
    hits = sum(bool(re.search(p, lc)) for p in CLICKBAIT_WORDS)
    score = hits * 12

    # many exclamations add up to 30
    excls = h.count("!")
    if excls >= 3:
        score += 30
    elif excls == 2:
        score += 20
    elif excls == 1:
        score += 10

    # ALL CAPS ratio penalty (ignoring small words)
    tokens = re.findall(r"[A-Za-z]+", h)
    if tokens:
        caps = [t for t in tokens if len(t) >= 3 and t.isupper()]
        ratio = len(caps) / len(tokens)
        if ratio >= 0.5:
            score += 30
        elif ratio >= 0.3:
            score += 20
        elif ratio >= 0.15:
            score += 10

    # clamp
    return max(0, min(100, int(score)))