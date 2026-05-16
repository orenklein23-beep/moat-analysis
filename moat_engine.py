import os
from datetime import datetime

import streamlit as st
from openai import OpenAI

# =========================
# SAFE API KEY SETUP
# =========================

api_key = None

# Try local environment first
try:
    api_key = os.getenv("GROQ_API_KEY")
except:
    pass

# Try Streamlit secrets second
try:
    if not api_key:
        api_key = st.secrets.get("GROQ_API_KEY")
except:
    pass

# Final safety check
if not api_key:
    st.error("GROQ_API_KEY not found.")
    st.stop()

# =========================
# OPENAI / GROQ CLIENT
# =========================

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# =========================
# SESSION HISTORY
# =========================

if "history" not in st.session_state:
    st.session_state["history"] = []

# =========================
# SAVE HISTORY
# =========================

def save_history(company, analysis_type):

    entry = {
        "company": company,
        "type": analysis_type,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    st.session_state["history"].append(entry)

# =========================
# GET HISTORY
# =========================

def get_history():

    if "history" not in st.session_state:
        return []

    return list(reversed(st.session_state["history"]))

# =========================
# SINGLE MOAT ANALYSIS
# =========================

def analyze_moat(company):

    prompt = f"""
You are an elite institutional equity analyst.

Deeply analyze the competitive moat of {company}.

Analyze:
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

For EACH:
- score out of 10
- explanation
- moat risks

Then provide:
- overall moat score out of 100
- moat durability
- biggest strength
- biggest weakness
- 5-year outlook
- investment conclusion

Professional hedge-fund tone.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a world-class moat analyst."
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
Compare the competitive moats of these companies:

{company_text}

For each company analyze:
- Brand
- Network effects
- Switching costs
- Ecosystem
- Pricing power
- Durability
- Weaknesses

Then provide:
1. strongest moat ranking
2. moat explanations
3. moat expansion potential
4. final winner

Professional investment tone.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an institutional moat strategist."
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
Give {company} a moat score from 0 to 100.

Include:
- brand
- switching costs
- network effects
- pricing power
- durability

Return:
Score: X/100
Reason: explanation
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a moat scoring engine."
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

Discuss:
- dominance
- competitors
- disruption risk
- market durability
- long-term compounding potential
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an industry structure analyst."
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
# MOAT EXPANSION
# =========================

def moat_expansion(company):

    prompt = f"""
Analyze whether {company}'s moat is:
- expanding
- stable
- shrinking

Discuss:
- AI
- ecosystem
- customer lock-in
- strategic positioning
- future durability
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a moat trajectory analyst."
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
