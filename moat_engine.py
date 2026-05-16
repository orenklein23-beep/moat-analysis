import os
from datetime import datetime

import streamlit as st
from openai import OpenAI

# =========================
# API SETUP
# =========================

api_key = os.getenv("GROQ_API_KEY")

try:
    if not api_key:
        api_key = st.secrets["GROQ_API_KEY"]
except:
    pass

if not api_key:
    st.error("Missing GROQ_API_KEY")
    st.stop()

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# =========================
# SESSION HISTORY
# =========================

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# SAVE HISTORY
# =========================

def save_history(company, analysis_type):

    st.session_state.history.append({
        "company": company,
        "type": analysis_type,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# =========================
# GET HISTORY
# =========================

def get_history():
    return st.session_state.history[::-1]

# =========================
# SINGLE MOAT ANALYSIS
# =========================

def analyze_moat(company):

    prompt = f"""
You are an elite institutional equity analyst.

Your job is to deeply analyze the competitive moat of {company}.

Analyze using these categories:

1. Brand Power
2. Network Effects
3. Switching Costs
4. Cost Advantages
5. Data Advantages
6. Ecosystem Lock-in
7. Management Quality
8. Pricing Power
9. Regulatory Advantages
10. Long-Term Survivability

For EACH category:
- Give a score out of 10
- Explain WHY
- Explain risks to the moat

Then provide:
- Overall moat score out of 100
- Moat durability rating
- Biggest strength
- Biggest weakness
- 5-year moat outlook
- Final investment-style conclusion

Formatting rules:
- Clean formatting
- No markdown tables
- No weird separators
- Professional hedge-fund tone
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a top-tier hedge fund moat analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=2500
    )

    save_history(company, "Single Analysis")

    return response.choices[0].message.content

# =========================
# COMPARE MOATS
# =========================

def compare_moats(companies):

    company_text = ", ".join(companies)

    prompt = f"""
You are an elite institutional investor.

Compare the competitive moats of these companies:

{company_text}

For EACH company analyze:
- Brand
- Network Effects
- Switching Costs
- Ecosystem
- Pricing Power
- Data Advantages
- Durability
- Weaknesses

Then provide:
1. Ranking from strongest moat to weakest
2. Explanation for rankings
3. Most undervalued moat
4. Most overestimated moat
5. Which company has the highest probability of moat expansion over 10 years
6. Final winner

Formatting:
- Clean UI-friendly formatting
- No markdown tables
- Professional investment tone
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a world-class moat strategist."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=3000
    )

    save_history(company_text, "Comparison")

    return response.choices[0].message.content

# =========================
# MOAT SCORE
# =========================

def moat_score(company):

    prompt = f"""
Give {company} a moat strength score from 0 to 100.

Scoring factors:
- Brand
- Network effects
- Switching costs
- Ecosystem lock-in
- Pricing power
- Competitive positioning
- Durability
- Capital intensity barriers

Return ONLY this format:

Score: X/100
Reason: short explanation
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an institutional moat scoring engine."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content

# =========================
# INDUSTRY POSITIONING
# =========================

def industry_position(company):

    prompt = f"""
Analyze the industry positioning of {company}.

Include:
- Competitive advantages
- Industry dominance
- Key competitors
- Market structure
- Risk of disruption
- Market share durability
- Ability to compound over 10 years

Professional investment tone.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an elite market structure analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=1800
    )

    return response.choices[0].message.content

# =========================
# MOAT EXPANSION ANALYSIS
# =========================

def moat_expansion(company):

    prompt = f"""
Analyze whether {company}'s moat is expanding or shrinking.

Discuss:
- AI advantages
- Ecosystem expansion
- Customer lock-in trends
- Margins
- Strategic positioning
- International expansion
- Competitive threats
- Future moat trajectory

Then conclude:
- Expanding
- Stable
- Shrinking

Explain why.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a long-term moat trajectory analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=1800
    )

    return response.choices[0].message.content
