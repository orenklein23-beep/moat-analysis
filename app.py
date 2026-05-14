import streamlit as st
from moat_engine import (
    analyze_moat,
    compare_moats,
    get_history
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="MoatIQ Terminal",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0e1117;
    color: white;
    font-family: Arial;
}

.main {
    background-color: #0e1117;
}

h1, h2, h3 {
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #222;
}

.stButton>button {
    background-color: #f59e0b;
    color: black;
    border-radius: 8px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #fbbf24;
    color: black;
}

.metric-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #222;
    margin-bottom: 20px;
}

.result-box {
    background-color: #111827;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #333;
    margin-top: 20px;
    line-height: 1.7;
}

.small-text {
    color: #9ca3af;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------
st.title("🧠 MoatIQ Terminal")

st.markdown("""
<div class="small-text">
Institutional Competitive Advantage Research System
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------
# SIDEBAR
# -----------------------------------
mode = st.sidebar.selectbox(
    "Research Mode",
    [
        "Single Analysis",
        "Compare Companies",
        "Peer Benchmark",
        "History Tracker"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### System")
st.sidebar.markdown("Model: Llama 3.3 70B")
st.sidebar.markdown("Framework: Institutional Moat Analysis")
st.sidebar.markdown("Version: v5")

# -----------------------------------
# SINGLE ANALYSIS
# -----------------------------------
if mode == "Single Analysis":

    st.subheader("Single Company Moat Analysis")

    company = st.text_input(
        "Company",
        placeholder="Apple"
    )

    if st.button("Run Analysis"):

        with st.spinner("Running institutional moat analysis..."):

            result = analyze_moat(company)

        st.markdown("""
        <div class="result-box">
        """, unsafe_allow_html=True)

        st.write(result)

        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------
# COMPARE MODE
# -----------------------------------
elif mode == "Compare Companies":

    st.subheader("Company Comparison")

    col1, col2 = st.columns(2)

    with col1:
        c1 = st.text_input("Company 1", "Apple")

    with col2:
        c2 = st.text_input("Company 2", "Microsoft")

    if st.button("Compare Moats"):

        with st.spinner("Comparing competitive advantages..."):

            result = compare_moats([c1, c2])

        st.markdown("""
        <div class="result-box">
        """, unsafe_allow_html=True)

        st.write(result)

        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------
# PEER BENCHMARK
# -----------------------------------
elif mode == "Peer Benchmark":

    st.subheader("Peer Benchmark Ranking")

    companies = st.text_area(
        "Enter Companies",
        "Apple, Microsoft, Google"
    )

    if st.button("Rank Companies"):

        with st.spinner("Ranking moat strength..."):

            result = compare_moats(companies)

        st.markdown("""
        <div class="result-box">
        """, unsafe_allow_html=True)

        st.write(result)

        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------
# HISTORY TRACKER
# -----------------------------------
elif mode == "History Tracker":

    st.subheader("Historical Analysis Archive")

    company = st.text_input(
        "Company",
        "Apple"
    )

    if st.button("Load History"):

        history = get_history(company)

        if not history:
            st.warning("No history available yet.")

        else:

            for item in reversed(history[-10:]):

                st.markdown(f"""
                <div class="result-box">
                <h4>{item['timestamp']}</h4>
                """, unsafe_allow_html=True)

                st.write(item["result"])

                st.markdown("</div>", unsafe_allow_html=True)