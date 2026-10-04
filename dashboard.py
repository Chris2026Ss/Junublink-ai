import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="JunubLink AI | Juba Dashboard",
    page_icon="🇸🇸",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Demo analytics for the local dashboard
analytics = {
    "sections": {
        "Jobs": 132,
        "Scholarships": 86,
        "Market Prices": 94,
        "Scam Check": 67,
        "FAQ": 58,
        "Contact": 21,
    },
    "locations": {
        "Juba": 128,
        "Wau": 34,
        "Malakal": 18,
        "Bentiu": 12,
        "Remote": 22,
    },
    "daily_visits": [
        {"date": "2026-09-25", "visits": 22},
        {"date": "2026-09-26", "visits": 28},
        {"date": "2026-09-27", "visits": 31},
        {"date": "2026-09-28", "visits": 40},
        {"date": "2026-09-29", "visits": 45},
        {"date": "2026-09-30", "visits": 52},
        {"date": "2026-10-01", "visits": 58},
        {"date": "2026-10-02", "visits": 67},
        {"date": "2026-10-03", "visits": 70},
        {"date": "2026-10-04", "visits": 79},
    ],
    "scam_alerts": [
        {"type": "Upfront payment", "count": 25},
        {"type": "Urgent message", "count": 14},
        {"type": "Unusual payment method", "count": 18},
        {"type": "No official contact", "count": 12},
    ],
    "jobs_viewed": [
        {"job": "Community Health Volunteer", "views": 48},
        {"job": "Digital Skills Trainer", "views": 41},
        {"job": "English Tutor", "views": 35},
        {"job": "Mobile Money Agent", "views": 27},
    ],
}

st.set_page_config(
    page_title="JunubLink AI Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 JunubLink AI Dashboard")
st.caption("Juba-focused usage overview for opportunity discovery and scam awareness")

# KPI cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total visits", "1,254")
col2.metric("Scam checks", "278")
col3.metric("Jobs viewed", "482")
col4.metric("Top location", "Juba")

# Page sections
st.subheader("1. Section usage")
sections_df = pd.DataFrame(
    [{"Section": k, "Views": v} for k, v in analytics["sections"].items()]
)
st.bar_chart(sections_df.set_index("Section"))

st.subheader("2. Visitor locations")
locations_df = pd.DataFrame(
    [{"Location": k, "Users": v} for k, v in analytics["locations"].items()]
)
st.bar_chart(locations_df.set_index("Location"))

st.subheader("3. Daily traffic")
daily_df = pd.DataFrame(analytics["daily_visits"])
st.line_chart(daily_df.set_index("date"))

st.subheader("4. Scam pattern reports")
scam_df = pd.DataFrame(analytics["scam_alerts"])
st.bar_chart(scam_df.set_index("type"))

st.subheader("5. Most-viewed jobs")
job_df = pd.DataFrame(analytics["jobs_viewed"])
st.bar_chart(job_df.set_index("job"))

st.markdown("---")
st.caption("Demo dashboard for JunubLink AI. Replace demo data with live analytics when connected to a database or analytics backend.")
