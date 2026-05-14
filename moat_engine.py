import os
import json
from datetime import datetime
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

HISTORY_FILE = "moat_history.json"

# -----------------------------
# HISTORY SYSTEM
# -----------------------------
def load_history():
    try:
        if not os.path.exists(HISTORY_FILE):
            return {}

        with open(HISTORY_FILE, "r") as f:
            return json.load(f)

    except:
        return {}


def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


# -----------------------------
# INDUSTRY WEIGHTS
# -----------------------------
INDUSTRY_WEIGHTS = {
    "default": {
        "focus": "balanced"
    },
    "saas": {
        "focus": "switching costs and network effects"
    },
    "consumer": {
        "focus": "brand and pricing power"
    },
    "semiconductor": {
        "focus": "scale advantage"
    },
    "financials": {
        "focus": "scale and pricing power"
    }
}


# -----------------------------
# INDUSTRY DETECTION
# -----------------------------
def detect_industry(company):

    c = company.lower()

    if any(x in c for x in ["apple", "microsoft", "google", "salesforce"]):
        return "saas"

    if any(x in c for x in ["nike", "coca", "pepsi", "lvmh"]):
        return "consumer"

    if any(x in c for x in ["nvidia", "amd", "intel"]):
        return "semiconductor"

    if any(x in c for x in ["jpmorgan", "visa", "mastercard"]):
        return "financials"

    return "default"


# -----------------------------
# SYSTEM PROMPT
# -----------------------------
MOAT_PROMPT = """
You are a senior hedge fund equity analyst.

Evaluate competitive advantages using institutional-level reasoning.

CORE REQUIREMENTS:
- Be skeptical
- Avoid hype
- Avoid inflated scores
- Detect fragile or cyclical advantages

MOAT CATEGORIES:
- Switching Costs
- Network Effects
- Pricing Power
- Brand Strength
- Scale Advantage
- Regulatory Barriers

SCORING:
0–2 = no moat
3–4 = weak
5–6 = average
7–8 = strong
9–10 = exceptional

IMPORTANT:
Final moat score MUST logically align with category analysis.

EDGE CASE DETECTION:
Flag:
- hype-driven narratives
- cyclical businesses
- temporary advantages
- weak durability

OUTPUT FORMAT:

Moat Score: X/10
Moat Tier: Elite / Strong / Average / Weak
Moat Durability: Short / Medium / Long

Switching Costs: explanation
Network Effects: explanation
Pricing Power: explanation
Brand Strength: explanation
Scale Advantage: explanation
Regulatory Barriers: explanation

Industry Context:
- explain industry-specific moat importance

Moat Risks:
- bullets

Edge Case Flags:
- bullets

Conclusion:
1–2 sentence institutional verdict
"""


# -----------------------------
# CONSISTENCY AUDIT
# -----------------------------
def consistency_check(result):

    prompt = f"""
Audit this moat analysis.

Check:
- score consistency
- overrating
- weak reasoning
- hype bias

Return short audit summary.

Analysis:
{result}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You audit financial reasoning."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# -----------------------------
# SINGLE ANALYSIS
# -----------------------------
def analyze_moat(company):

    industry = detect_industry(company)

    focus = INDUSTRY_WEIGHTS[industry]["focus"]

    prompt = f"""
Analyze company: {company}

Industry: {industry}

Important industry moat focus:
{focus}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": MOAT_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    audit = consistency_check(result)

    final_result = result + "\n\nConsistency Audit:\n" + audit

    # SAVE HISTORY
    history = load_history()

    if company not in history:
        history[company] = []

    history[company].append({
        "timestamp": str(datetime.now()),
        "result": final_result
    })

    save_history(history)

    return final_result


# -----------------------------
# COMPARISON MODE
# -----------------------------
def compare_moats(companies):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": MOAT_PROMPT},
            {
                "role": "user",
                "content": f"Compare moat strength of these companies: {companies}"
            }
        ]
    )

    return response.choices[0].message.content


# -----------------------------
# HISTORY RETRIEVAL
# -----------------------------
def get_history(company):

    history = load_history()

    return history.get(company, [])