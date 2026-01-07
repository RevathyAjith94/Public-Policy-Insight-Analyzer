import streamlit as st

from src.ingestion import ingest_bill
from src.preprocessing import preprocess_text
from src.classifier import classify_bill
from src.chronology import extract_related_acts
from src.impact import analyze_impact
from src.summarizer import generate_summary


st.set_page_config(
    page_title="Public Policy Insight & Impact Analyzer",
    layout="wide"
)

st.title("📜 Public Policy Insight & Impact Analyzer (PPIIA)")
st.caption("Simplifying Government Bills for Every Citizen")

st.markdown("---")


st.sidebar.title("ℹ️ About")
st.sidebar.write("""
This AI-powered platform analyzes Indian government bills and converts them into
easy-to-understand summaries for citizens, businesses, and researchers.
""")

st.sidebar.markdown("**Domain:** CivicTech / Public Policy Analytics")
st.sidebar.markdown("**Tech:** NLP · LLM · Streamlit")


st.subheader("📥 Upload Bill")

uploaded_file = st.file_uploader(
    "Upload Government Bill PDF",
    type=["pdf"]
)

st.markdown("### OR")

bill_url = st.text_input(
    "Paste Official Bill URL (sansad.in)"
)

analyze_btn = st.button("🔍 Analyze Bill")

st.markdown("---")


if analyze_btn:

    if not uploaded_file and not bill_url:
        st.error("⚠️ Please upload a PDF or provide a valid bill URL.")
    else:
        with st.spinner("Analyzing bill... Please wait ⏳"):

            if uploaded_file:
                bill_data = ingest_bill("pdf", uploaded_file)
            else:
                bill_data = ingest_bill("url", bill_url)

            raw_text = bill_data.get("raw_text", "")

            structured_text = preprocess_text(raw_text)

            category_result = classify_bill(raw_text)

            chronology_result = extract_related_acts(raw_text)

            impact_result = analyze_impact(raw_text)

            try:
                summary_result = generate_summary(raw_text)
            except Exception as e:
                summary_result = {
                    "citizen_summary": "⚠️ LLM summary unavailable. Please check API key."
                }

        st.success("✅ Analysis completed successfully!")

       
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📌 Bill Category")
            st.write(f"**Category:** {category_result.get('bill_category')}")
            st.write(f"**Confidence:** {category_result.get('confidence')}")

        with col2:
            st.subheader("🕰️ Related Acts & Amendments")
            acts = chronology_result.get("related_acts", [])
            if acts:
                for act in acts:
                    st.write(f"- {act}")
            else:
                st.write("No related acts detected.")

        st.markdown("---")

        st.subheader("📊 Impact Analysis")
        st.write("**Affected Sectors:**", ", ".join(impact_result.get("affected_sectors", [])))
        st.write("**Citizen Impact:**", impact_result.get("citizen_impact"))
        st.write("**Business Impact:**", impact_result.get("business_impact"))
        st.write("**Government Impact:**", impact_result.get("government_impact"))

        st.markdown("---")

        st.subheader("🧾 Citizen-Friendly Summary")
        st.write(summary_result.get("citizen_summary"))

        st.markdown("---")

        st.subheader("📂 Extracted Sections (Optional View)")
        with st.expander("Click to view structured bill sections"):
            for key, value in structured_text.get("sections", {}).items():
                st.markdown(f"**{key.upper()}**")
                st.write(value)
                st.markdown("---")
