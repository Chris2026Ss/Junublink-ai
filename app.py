import streamlit as st

st.set_page_config(
    page_title="JunubLink AI | Juba",
    page_icon="🇸🇸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(90deg, #0b5394, #1f7a8c);
        color: white;
        padding: 2rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        text-align: center;
    }
    .section-box {
        background: #f8f9fa;
        border: 1px solid #dfe3e8;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .metric-box {
        background: #eef7ff;
        border-radius: 10px;
        padding: 1rem;
        border-left: 5px solid #1f77b4;
    }
    .success-box {
        background: #ebf9f0;
        border: 1px solid #9ad7b6;
        border-radius: 10px;
        padding: 0.75rem;
    }
    .warning-box {
        background: #fff5e6;
        border: 1px solid #ffd28a;
        border-radius: 10px;
        padding: 0.75rem;
    }
    .danger-box {
        background: #fdecea;
        border: 1px solid #f5b7b1;
        border-radius: 10px;
        padding: 0.75rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='main-header'>
        <h1>🇸🇸 JunubLink AI</h1>
        <p>Juba-first opportunities, verified local information, and more trust for South Sudan</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Menu")
page = st.sidebar.radio(
    "Choose a section",
    [
        "Home",
        "Jobs in Juba",
        "Scholarships & Training",
        "Market Prices",
        "Scam Check",
        "FAQ",
        "Contact",
    ],
)

jobs = [
    {
        "title": "Community Health Volunteer",
        "location": "Juba",
        "type": "Volunteer / stipend",
        "deadline": "14 days",
        "summary": "Support outreach and awareness activities in clinics and communities.",
        "contact": "Ministry of Health offices / local NGO partners",
    },
    {
        "title": "Digital Skills Trainer",
        "location": "Juba",
        "type": "Contract",
        "deadline": "21 days",
        "summary": "Teach youth basic computer use, digital literacy, and job-readiness skills.",
        "contact": "NGO training centers and youth centers",
    },
    {
        "title": "English Tutor",
        "location": "Juba",
        "type": "Part-time",
        "deadline": "Ongoing",
        "summary": "Teach English and communication skills to students and young professionals.",
        "contact": "Student groups, schools, and private tutoring networks",
    },
    {
        "title": "Mobile Money Agent",
        "location": "Juba",
        "type": "Commission-based",
        "deadline": "30 days",
        "summary": "Help people send, receive, and manage mobile money transfers safely.",
        "contact": "MTN/Zain service centers in Juba",
    },
]

scholarships = [
    {
        "title": "Youth Digital Skills Program",
        "provider": "Local NGO / education partner",
        "location": "Juba",
        "deadline": "Rolling",
        "summary": "Training in digital literacy, online safety, and job preparation.",
    },
    {
        "title": "Entrepreneurship Bootcamp",
        "provider": "Business support group",
        "location": "Juba",
        "deadline": "This month",
        "summary": "Support for small traders and youth-led business ideas.",
    },
    {
        "title": "Community Health Training",
        "provider": "Health NGO",
        "location": "Juba",
        "deadline": "Next intake",
        "summary": "Hands-on toolkits for community health education and outreach.",
    },
]

market_prices = [
    {"item": "Maize", "price": "SSP 2,000-2,500 / bag", "location": "Juba Central Market"},
    {"item": "Rice", "price": "SSP 2,500-3,000 / bag", "location": "Juba Central Market"},
    {"item": "Sugar", "price": "SSP 400-500 / kg", "location": "Konyo-Konyo Market"},
    {"item": "Fuel", "price": "SSP 3,800-4,200 / liter", "location": "Juba fuel stations"},
    {"item": "Cooking oil", "price": "SSP 900-1,100 / liter", "location": "Juba Central Market"},
    {"item": "Tomatoes", "price": "SSP 500-800 / basket", "location": "Konyo-Konyo Market"},
]


def scam_score(message: str):
    msg = message.lower()
    score = 0
    warnings = []

    if any(word in msg for word in ["urgent", "act now", "hurry", "limited time"]):
        score += 1
        warnings.append("Urgency pressure")
    if any(word in msg for word in ["pay first", "registration fee", "processing fee", "security deposit"]):
        score += 3
        warnings.append("Requests payment before you confirm details")
    if any(word in msg for word in ["guaranteed income", "easy money", "quick cash", "no work"]):
        score += 2
        warnings.append("Promise of unrealistic earnings")
    if any(word in msg for word in ["bitcoin", "western union", "crypto", "cash app"]):
        score += 2
        warnings.append("Untraceable or unusual payment method")
    if any(word in msg for word in ["whatsapp only", "dm me", "private message", "no office"]):
        score += 1
        warnings.append("No clear official contact details")
    if any(word in msg for word in ["i am abroad", "from abroad", "foreign partner", "sponsor"]):
        score += 1
        warnings.append("Possible impersonation or outside contact")

    return score, warnings


if page == "Home":
    st.subheader("Welcome to JunubLink AI")
    st.write(
        "JunubLink AI helps Juba residents discover trusted jobs, training, market information, and safety support in one simple platform."
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Jobs", len(jobs))
    col2.metric("Scholarships", len(scholarships))
    col3.metric("Market items", len(market_prices))
    col4.metric("Focus", "Juba")

    st.markdown("""
    <div class='section-box'>
        <h3>Why this matters in Juba</h3>
        <ul>
            <li>Young people need trusted jobs and training.</li>
            <li>Traders need current market prices.</li>
            <li>Many scams look real when they use urgency and payment requests.</li>
            <li>People often look for answers through WhatsApp, local groups, and community networks.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "Jobs in Juba":
    st.subheader("Jobs in Juba")
    st.info("The focus is on Juba-based opportunities and ways to verify them before applying.")

    for job in jobs:
        st.markdown("""
        <div class='section-box'>
            <h4>{title}</h4>
            <p><strong>Location:</strong> {location}</p>
            <p><strong>Type:</strong> {type}</p>
            <p><strong>Deadline:</strong> {deadline}</p>
            <p><strong>Summary:</strong> {summary}</p>
            <p><strong>How to apply:</strong> {contact}</p>
        </div>
        """.format(
            title=job["title"],
            location=job["location"],
            type=job["type"],
            deadline=job["deadline"],
            summary=job["summary"],
            contact=job["contact"],
        ), unsafe_allow_html=True)

elif page == "Scholarships & Training":
    st.subheader("Scholarships & training opportunities")
    st.success("These are ideal for students, young professionals, and youth groups in Juba.")

    for item in scholarships:
        st.markdown("""
        <div class='section-box'>
            <h4>{title}</h4>
            <p><strong>Provider:</strong> {provider}</p>
            <p><strong>Location:</strong> {location}</p>
            <p><strong>Deadline:</strong> {deadline}</p>
            <p><strong>Details:</strong> {summary}</p>
        </div>
        """.format(
            title=item["title"],
            provider=item["provider"],
            location=item["location"],
            deadline=item["deadline"],
            summary=item["summary"],
        ), unsafe_allow_html=True)

elif page == "Market Prices":
    st.subheader("Market prices in Juba")
    st.warning("Prices should be treated as quick local references and verified by traders or local markets.")

    for item in market_prices:
        st.markdown(
            f"<div class='section-box'><strong>{item['item']}</strong><br>{item['price']}<br><small>{item['location']}</small></div>",
            unsafe_allow_html=True,
        )

elif page == "Scam Check":
    st.subheader("Scam Check")
    st.write("Paste a job or scholarship message to check for risky signs before paying money or giving personal information.")

    text = st.text_area("Offer message", height=180, placeholder="Example: Pay SSP 5,000 registration fee now and get a guaranteed monthly salary.")

    if st.button("Check risk"):
        if not text.strip():
            st.warning("Please paste the message first.")
        else:
            score, warnings = scam_score(text)
            if score >= 6:
                st.markdown("<div class='danger-box'><strong>High risk:</strong> this message looks suspicious. Do not send money.</div>", unsafe_allow_html=True)
            elif score >= 3:
                st.markdown("<div class='warning-box'><strong>Moderate risk:</strong> verify before proceeding.</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='success-box'><strong>Low risk:</strong> no obvious scam patterns detected.</div>", unsafe_allow_html=True)

            if warnings:
                st.write("Warning signs found:")
                for w in warnings:
                    st.write(f"- {w}")

            st.write("Safety tips: verify the provider, contact official offices, and never pay first before confirming the offer.")

elif page == "FAQ":
    st.subheader("Frequently asked questions")

    with st.expander("How do I know if a job is real?"):
        st.write("Ask for the organization name, office location, contact number, and a written description. Do not send money before verifying.")

    with st.expander("How can I protect myself from scams?"):
        st.write("Never pay upfront for a job or scholarship. Confirm the sender and check whether the organization exists in person or on official channels.")

    with st.expander("Why focus on Juba?"):
        st.write("Juba is the main urban hub in South Sudan, so most opportunities, offices, schools, and NGOs are concentrated there. A local-first approach helps people use the app more easily.")

    with st.expander("Can this app help traders?"):
        st.write("Yes. Traders can use the market price section to compare costs and check local pricing trends before trading.")

elif page == "Contact":
    st.subheader("Contact & support")
    st.write("This project is still early-stage. You can use this page to share ideas, support requests, or opportunities to add.")

    name = st.text_input("Name")
    email = st.text_input("Email (optional)")
    message = st.text_area("Message")

    if st.button("Send message"):
        if message.strip():
            st.success("Thank you for your message. JunubLink AI will review it.")
        else:
            st.warning("Please write a message before sending.")

st.markdown("---")
st.caption("JunubLink AI — Juba-first local information for opportunity, trust, and community support.")
