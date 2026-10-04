import streamlit as st

st.set_page_config(
    page_title="JunubLink AI",
    page_icon="🇸🇸",
    layout="wide",
)

st.title("JunubLink AI")
st.caption("Connecting South Sudanese communities with opportunities, information, and support")

# Sample data
jobs = [
    {
        "title": "Community Health Outreach Volunteer",
        "location": "Juba",
        "type": "Volunteer",
        "deadline": "14 days",
        "summary": "Support public health outreach in local communities.",
    },
    {
        "title": "Digital Skills Trainer",
        "location": "Wau",
        "type": "Contract",
        "deadline": "21 days",
        "summary": "Train youth in digital literacy and basic business tools.",
    },
]

scholarships = [
    {
        "title": "Youth Leadership Scholarship",
        "provider": "Local education program",
        "location": "Remote / Juba",
        "deadline": "10 days",
        "summary": "For youth leaders active in community projects.",
    },
    {
        "title": "Women in Tech Bootcamp",
        "provider": "Digital inclusion initiative",
        "location": "Hybrid",
        "deadline": "7 days",
        "summary": "Training and mentorship for women exploring digital careers.",
    },
]

market_prices = [
    {"item": "Maize", "price": "SSP 1,800 / bag", "location": "Juba"},
    {"item": "Rice", "price": "SSP 2,200 / bag", "location": "Juba"},
    {"item": "Fuel", "price": "SSP 4,100 / liter", "location": "Wau"},
]


def scam_score(message: str) -> int:
    msg = message.lower()
    score = 0

    if "urgent" in msg or "pay first" in msg:
        score += 2
    if "cash app" in msg or "bitcoin" in msg or "crypto" in msg:
        score += 2
    if "guaranteed" in msg or "easy money" in msg:
        score += 2
    if "i am" in msg and "from" in msg and "abroad" in msg:
        score += 1
    if "contact me on whatsapp" in msg and "no interview" in msg:
        score += 1
    if "pay" in msg and "registration" in msg:
        score += 2

    return score


col1, col2, col3 = st.columns(3)
col1.metric("Jobs", str(len(jobs)))
col2.metric("Scholarships", str(len(scholarships)))
col3.metric("Market Items", str(len(market_prices)))

st.write("")

job_tab, scholarship_tab, market_tab, scam_tab = st.tabs([
    "Opportunities",
    "Scholarships",
    "Market prices",
    "Scam check",
])

with job_tab:
    for item in jobs:
        with st.container():
            st.subheader(item["title"])
            st.write(f"Location: {item['location']} | Type: {item['type']} | Deadline: {item['deadline']}")
            st.write(item["summary"])
            st.write("---")

with scholarship_tab:
    for item in scholarships:
        with st.container():
            st.subheader(item["title"])
            st.write(f"Provider: {item['provider']} | Location: {item['location']} | Deadline: {item['deadline']}")
            st.write(item["summary"])
            st.write("---")

with market_tab:
    for item in market_prices:
        st.write(f"- {item['item']} in {item['location']}: **{item['price']}**")

with scam_tab:
    offer_text = st.text_area(
        "Paste a job, scholarship, or offer message",
        placeholder="Example: We need a person to pay a registration fee and receive cash from a secret client.",
        height=180,
    )

    if st.button("Check offer"):
        if not offer_text.strip():
            st.warning("Please paste an offer message first.")
        else:
            score = scam_score(offer_text)
            if score >= 5:
                st.error(f"High risk: this message looks suspicious (score: {score}/10)")
                st.write("Tips: avoid upfront payments, verify the sender, and ask for official contact details.")
            elif score >= 3:
                st.warning(f"Moderate risk: this message needs verification (score: {score}/10)")
            else:
                st.success(f"Low risk: no obvious scam patterns detected (score: {score}/10)")

st.write("---")
st.markdown(
    "Built for South Sudan communities to discover opportunities, verify information, and reduce missing opportunities due to limited access to trusted information."
)


if __name__ == "__main__":
    pass
