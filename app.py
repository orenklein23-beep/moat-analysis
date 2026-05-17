import streamlit as st

from moat_engine import (
    analyze_moat,
    compare_moats,
    moat_score,
    industry_position,
    moat_expansion
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Moatiq",
    page_icon="🧠",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #0e1117;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

h1 {
    font-size: 3rem;
    font-weight: 700;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-size: 16px;
    font-weight: 600;
}

.stTextInput > div > div > input {
    border-radius: 12px;
}

.result-box {
    background-color: #111827;
    padding: 25px;
    border-radius: 16px;
    margin-top: 20px;
    border: 1px solid #222;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.title("🧠 Moatiq")
st.caption("AI-Powered Competitive Moat Intelligence")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Mode")

mode = st.sidebar.radio(
    "Choose Analysis Type",
    [
        "Single Company",
        "Compare Companies",
        "Moat Score",
        "Industry Position",
        "Moat Expansion"
    ]
)

# =========================
# SINGLE COMPANY
# =========================

if mode == "Single Company":

    st.subheader("Single Company Moat Analysis")

    company = st.text_input(
        "Enter Company Name",
        placeholder="Apple"
    )

    if st.button("Analyze Moat"):

        if company:

            with st.spinner("Analyzing moat..."):

                result = analyze_moat(company)

            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================
# COMPARE COMPANIES
# =========================

elif mode == "Compare Companies":

    st.subheader("Compare Competitive Moats")

    companies = st.text_input(
        "Enter Companies (comma separated)",
        placeholder="Apple, Microsoft, Google"
    )

    if st.button("Compare Moats"):

        if companies:

            company_list = [
                c.strip() for c in companies.split(",")
            ]

            with st.spinner("Comparing moats..."):

                result = compare_moats(company_list)

            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================
# MOAT SCORE
# =========================

elif mode == "Moat Score":

    st.subheader("Moat Strength Score")

    company = st.text_input(
        "Enter Company",
        placeholder="Amazon"
    )

    if st.button("Generate Score"):

        if company:

            with st.spinner("Scoring moat..."):

                result = moat_score(company)

            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================
# INDUSTRY POSITION
# =========================

elif mode == "Industry Position":

    st.subheader("Industry Positioning Analysis")

    company = st.text_input(
        "Enter Company",
        placeholder="NVIDIA"
    )

    if st.button("Analyze Industry Position"):

        if company:

            with st.spinner("Analyzing industry positioning..."):

                result = industry_position(company)

            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================
# MOAT EXPANSION
# =========================

elif mode == "Moat Expansion":

    st.subheader("Moat Expansion Analysis")

    company = st.text_input(
        "Enter Company",
        placeholder="Meta"
    )

    if st.button("Analyze Expansion"):

        if company:

            with st.spinner("Analyzing moat trajectory..."):

                result = moat_expansion(company)

            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption("Moatiq • AI Moat Intelligence Platform")
