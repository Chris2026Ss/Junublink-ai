import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="JunuBlink AI", layout="wide")

# Language Toggle
col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
with col3:
    language = st.selectbox("Language", ["English", "العربية (Juba Arabic)"], key="lang")

# Translations
translations = {
    "English": {
        "title": "🎓 JunuBlink AI - Scholarship & Grant Finder",
        "subtitle": "Smart Matching for South Sudanese Youth",
        "your_info": "📋 Your Information",
        "first_name": "First Name",
        "last_name": "Last Name",
        "age": "Age",
        "location": "State/Location in South Sudan",
        "gender": "Gender",
        "email": "Email Address",
        "academic": "📚 Academic Background",
        "education_level": "Current Education Level",
        "gpa": "Academic Performance (GPA/Average %)",
        "field_study": "Field of Interest",
        "languages": "Languages You Speak",
        "financial": "💰 Financial & Social Information",
        "financial_sit": "Financial Situation",
        "disability": "Do you have any disability?",
        "employment": "Employment Status",
        "refugee": "Are you a refugee or IDP?",
        "check_btn": "Check My Eligibility",
        "results": "🎯 Scholarship & Grant Results",
        "scam_alert": "⚠️ SCAM ALERT & WARNINGS",
        "next_steps": "📝 Next Steps",
        "download": "Download Results",
        "footer": "Built for South Sudan 🇸🇸"
    },
    "العربية (Juba Arabic)": {
        "title": "🎓 جنو بلينك AI - الزمالات والمنح",
        "subtitle": "مطابقة ذكية لشباب جنوب السودان",
        "your_info": "📋 معلوماتك الشخصية",
        "first_name": "الاسم الأول",
        "last_name": "الاسم الأخير",
        "age": "العمر",
        "location": "الولاية / الموقع في جنوب السودان",
        "gender": "الجنس",
        "email": "عنوان البريد الإلكتروني",
        "academic": "📚 الخلفية الأكاديمية",
        "education_level": "مستوى التعليم الحالي",
        "gpa": "الأداء الأكاديمي (%)",
        "field_study": "مجال الدراسة المفضل",
        "languages": "اللغات التي تتحدثها",
        "financial": "💰 الحالة المالية والاجتماعية",
        "financial_sit": "الحالة المالية",
        "disability": "هل لديك إعاقة ما؟",
        "employment": "حالة العمل",
        "refugee": "هل أنت لاجئ أو نازح داخليًا؟",
        "check_btn": "تحقق من أهليتي",
        "results": "🎯 نتائج الزمالات والمنح",
        "scam_alert": "⚠️ تنبيهات ضد الاحتيال",
        "next_steps": "📝 الخطوات التالية",
        "download": "تحميل النتائج",
        "footer": "مبني لجنوب السودان 🇸🇸"
    }
}

t = translations[language]

st.title(t["title"])
st.subheader(t["subtitle"])

# Sidebar
with st.sidebar:
    st.info("🔒 Your data is safe. We never share personal information.")
    st.markdown("---")
    st.markdown("**JunuBlink AI**")
    st.markdown("Connecting South Sudanese youth to scholarships, grants & opportunities")
    st.markdown("---")
    st.markdown("**Creator:** Kerwar Duop Yoam")

# ==================== SCAM ALERT SECTION ====================
with st.expander("⚠️ " + t["scam_alert"], expanded=False):
    st.warning("""
    **🚨 COMMON SCHOLARSHIP SCAMS TO AVOID:**

    ❌ **They ask for money upfront** - Legitimate scholarships are FREE
    ❌ **Guaranteed scholarship** - No one guarantees you'll win
    ❌ **Unclear organization** - Always verify the organization exists
    ❌ **Pressure to decide quickly** - Real scholarships give you time
    ❌ **Asking for sensitive info** - Don't share bank details with unknown sources
    ❌ **Too good to be true** - If it sounds fake, it probably is

    **✅ SAFE SIGNS:**
    - Official website with organization details
    - Contact with verified email (@un.org, @unhcr.org, etc)
    - No upfront payment required
    - Clear application process
    - Listed on trusted websites (UN, World Bank, etc)

    **🆘 REPORT SCAMS:**
    - Tell trusted elders/teachers
    - Report to local authorities
    - Contact organization directly to verify
    """)

st.header(t["your_info"])

col1, col2 = st.columns(2)

with col1:
    first_name = st.text_input(t["first_name"])
    age = st.number_input(t["age"], min_value=16, max_value=40, value=20)
    location = st.selectbox(
        t["location"],
        ["Juba", "Central Equatoria", "Eastern Equatoria", "Western Equatoria",
         "Upper Nile", "Unity", "Jonglei", "Lakes", "Warrap", "Northern Bahr El Ghazal", "Other"]
    )

with col2:
    last_name = st.text_input(t["last_name"])
    gender = st.selectbox(t["gender"], ["Male", "Female", "Prefer not to say"])
    email = st.text_input(t["email"])

# Academic Information
st.header(t["academic"])

col3, col4 = st.columns(2)

with col3:
    education_level = st.selectbox(
        t["education_level"],
        ["Secondary School", "High School Completed", "Diploma", "Undergraduate", "Postgraduate"]
    )
    gpa = st.slider(t["gpa"], 0.0, 100.0, 75.0, step=1.0)

with col4:
    field_of_study = st.selectbox(
        t["field_study"],
        ["Engineering", "Medicine/Health", "Business", "Agriculture", "Technology/IT",
         "Education", "Law", "Environmental Science", "Social Sciences", "Other"]
    )
    languages = st.multiselect(
        t["languages"],
        ["English", "Arabic", "Nuer", "Dinka", "Shilluk", "Bari", "Other"],
        default=["English"]
    )

# Financial & Social
st.header(t["financial"])

col5, col6 = st.columns(2)

with col5:
    financial_situation = st.selectbox(
        t["financial_sit"],
        ["Very Poor", "Poor", "Moderate", "Stable", "Comfortable"]
    )
    has_disability = st.checkbox(t["disability"])

with col6:
    employment_status = st.selectbox(
        t["employment"],
        ["Unemployed", "Part-time", "Full-time", "Self-employed", "Student"]
    )
    refugee_idp = st.checkbox(t["refugee"])

# ==================== MATCHING ENGINE ====================
st.header(t["results"])

if st.button("✨ " + t["check_btn"]):
    if not first_name or not email:
        st.error("Please fill in name and email")
    else:
        opportunities = []

        # SCHOLARSHIPS

        # 1. African Leadership Scholarship
        score1 = 0
        if 18 <= age <= 30: score1 += 25
        if gpa >= 70: score1 += 25
        if financial_situation in ["Very Poor", "Poor"]: score1 += 25
        if "English" in languages: score1 += 25

        opportunities.append({
            "Type": "Scholarship",
            "Name": "African Leadership Foundation",
            "Score": score1,
            "Deadline": "Rolling",
            "Award": "$5,000-$15,000",
            "Status": "✅ Eligible" if score1 >= 75 else "⚠️ Apply" if score1 >= 50 else "❌"
        })

        # 2. Tech4Africa Grant
        score2 = 0
        if field_of_study in ["Technology/IT", "Engineering"]: score2 += 30
        if age <= 28: score2 += 20
        if gpa >= 75: score2 += 25
        if "English" in languages: score2 += 25

        opportunities.append({
            "Type": "Tech Grant",
            "Name": "Tech4Africa Innovation Grant",
            "Score": score2,
            "Deadline": "Quarterly",
            "Award": "$2,000-$10,000",
            "Status": "✅ Eligible" if score2 >= 75 else "⚠️ Apply" if score2 >= 50 else "❌"
        })

        # 3. UNHCR Education Grant
        score3 = 0
        if refugee_idp: score3 += 40
        if gpa >= 65: score3 += 30
        if financial_situation != "Comfortable": score3 += 30

        opportunities.append({
            "Type": "Scholarship",
            "Name": "UNHCR Education Grant",
            "Score": score3,
            "Deadline": "Monthly",
            "Award": "$3,000-$12,000",
            "Status": "✅ Eligible" if score3 >= 75 else "⚠️ Apply" if score3 >= 50 else "❌"
        })

        # 4. Women in Leadership
        if gender == "Female":
            score4 = 0
            if 18 <= age <= 32: score4 += 25
            if gpa >= 70: score4 += 25
            if field_of_study in ["Business", "Law", "Education"]: score4 += 25
            if financial_situation in ["Very Poor", "Poor"]: score4 += 25

            opportunities.append({
                "Type": "Scholarship",
                "Name": "Women in Leadership South Sudan",
                "Score": score4,
                "Deadline": "June 30",
                "Award": "$4,000-$10,000",
                "Status": "✅ Eligible" if score4 >= 75 else "⚠️ Apply" if score4 >= 50 else "❌"
            })

        # 5. Disability & Inclusion
        if has_disability:
            score5 = 50
            if gpa >= 60: score5 += 25
            if 18 <= age <= 30: score5 += 25

            opportunities.append({
                "Type": "Grant",
                "Name": "Disability & Inclusive Education",
                "Score": score5,
                "Deadline": "Rolling",
                "Award": "$2,000-$8,000",
                "Status": "✅ Eligible" if score5 >= 75 else "⚠️ Apply" if score5 >= 50 else "❌"
            })

        # Display Results
        st.success(f"✅ Analysis complete for {first_name} {last_name}")

        df = pd.DataFrame(opportunities)
        st.dataframe(df, use_container_width=True)

        # Opportunities by type
        st.subheader("💰 Available by Type:")
        scholarships = df[df["Type"] == "Scholarship"]
        grants = df[df["Type"].isin(["Tech Grant", "Grant"])]

        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Scholarships Found", len(scholarships))
        with col_b:
            st.metric("Grants Found", len(grants))

        # Next Steps
        st.header(t["next_steps"])

        if language == "English":
            st.info("""
            **TO APPLY SAFELY:**

            1. **Verify Organization**
               - Check official website
               - Call their office number
               - Never trust unknown emails

            2. **Gather Documents**
               - Academic transcripts
               - Birth certificate/ID
               - Proof of residence
               - Letters of recommendation

            3. **Apply Online**
               - Go to official website
               - Use official application form
               - NEVER pay money upfront
               - Keep confirmation emails

            4. **Follow Up**
               - Check email weekly
               - Call organization to confirm
               - Join WhatsApp scholarship groups

            5. **Share with Others**
               - Tell friends about opportunities
               - Share verified links only
               - Help spot scams together
            """)
        else:
            st.info("""
            **طريقة التقديم الآمنة:**

            1. **تحقق من المنظمة**
               - تحقق من الموقع الرسمي
               - اتصل برقم مكتبهم
               - لا تثق في الرسائل غير المعروفة

            2. **جمع المستندات**
               - شهادات أكاديمية
               - بطاقة هوية / شهادة ميلاد
               - إثبات الإقامة
               - خطابات التوصية

            3. **التقديم أونلاين**
               - اذهب للموقع الرسمي
               - استخدم نموذج التقديم الرسمي
               - لا تدفع أموال مقدما
               - احتفظ برسائل التأكيد

            4. **المتابعة**
               - تحقق من البريد أسبوعيًا
               - اتصل بالمنظمة للتأكيد
               - انضم لمجموعات المنح على واتس

            5. **شارك مع الآخرين**
               - أخبر أصدقاءك عن الفرص
               - شارك الروابط الموثوقة فقط
               - ساعد في اكتشاف الاحتيال
            """)

        # Download Results
        if st.checkbox(t["download"]):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            results_text = f"""
JunuBlink AI - SCHOLARSHIP & GRANT ASSESSMENT
Date: {timestamp}
Name: {first_name} {last_name}
Email: {email}
Age: {age}

OPPORTUNITIES FOUND:
{df.to_string()}

SCAM WARNING: Only apply through official websites. Never pay upfront fees.
Always verify with the organization before applying.

Language: {language}
            """
            st.download_button(
                label="📥 Download Results",
                data=results_text,
                file_name=f"JunuBlink_{first_name}_{last_name}.txt"
            )

# Footer
st.markdown("---")
if language == "English":
    st.markdown("""
    **JunuBlink AI** 🇸🇸

    Helping South Sudanese youth find legitimate scholarships and grants safely.

    ⚠️ **Remember:** Legitimate scholarships are FREE. Never pay upfront.
    """)
else:
    st.markdown("""
    **جنو بلينك AI** 🇸🇸

    مساعدة شباب جنوب السودان في العثور على زمالات ومنح شرعية بأمان.

    ⚠️ **تذكر:** الزمالات الشرعية مجانية. لا تدفع أموالاً مقدماً.
    """)
