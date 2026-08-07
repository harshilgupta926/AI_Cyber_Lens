import streamlit as st
from groq import Groq
from pypdf import PdfReader


api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)

st.sidebar.divider()

# ---------- Custom CSS ----------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#07111f,#0b1f3a,#12294d);
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Title */
.title{
    text-align:center;
    font-size:52px;
    font-weight:800;
    color:white;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#8ec5ff;
    margin-bottom:25px;
}

.desc{
    text-align:center;
    color:#d6d6d6;
    font-size:18px;
    margin-bottom:35px;
}

/* Cards */
.card{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:18px;
    padding:22px;
    text-align:center;
    transition:0.3s;
    box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

.card:hover{
    transform:translateY(-5px);
    border:1px solid #3b82f6;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#071827;
}

/* Buttons */

.stButton>button{
    width:100%;
    border-radius:12px;
    height:52px;
    border:none;
    color:white;
    background:linear-gradient(90deg,#2563EB,#06B6D4);
    font-weight:bold;
    font-size:17px;
}

.stButton>button:hover{
    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------

st.markdown(
"""
<div class="title">
🛡️ AI Cyber Lens
</div>

<div class="subtitle">
AI Powered Cybersecurity Platform
</div>

<div class="desc">
Detect phishing, scams, deepfakes, fake news, malicious URLs,
QR codes, suspicious emails and PDF threats using AI.
</div>
""",
unsafe_allow_html=True
)

# ---------- Feature Cards ----------

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>📝 Text Scanner</h3>
    Detect scams and phishing messages.
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>🌐 URL Scanner</h3>
    Detect malicious and phishing websites.
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>🖼 Image Scanner</h3>
    Analyze screenshots and suspicious images.
    </div>
    """,unsafe_allow_html=True)

c4,c5,c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="card">
    <h3>📧 Email Scanner</h3>
    Detect fraudulent emails.
    </div>
    """,unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card">
    <h3>📄 PDF Scanner</h3>
    Analyze uploaded documents.
    </div>
    """,unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="card">
    <h3>🔳 QR Scanner</h3>
    Detect dangerous QR codes.
    </div>
    """,unsafe_allow_html=True)

st.divider()

# ---------- Sidebar ----------

st.sidebar.title("⚙️ Settings")

api_key = st.sidebar.text_input(
    "🔑 Groq API Key",
    type="password"
)

st.sidebar.divider()

user_profile = st.sidebar.selectbox(
    "👤 Who are you?",
    [
        "Student",
        "Senior Citizen",
        "Working Professional",
        "Business Owner",
        "Parent",
        "Government Employee",
        "Other"
    ]
)

st.sidebar.success("🛡️ Privacy First")




def read_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text



def analyze(text):

    client = Groq(
        api_key=api_key
    )


    prompt = f"""
You are AI Cyber Lens, an advanced AI-powered cybersecurity assistant that detects deepfakes, scams, phishing, fake news, impersonation, fraud, malware, spam, and other digital threats.

User Profile:
{user_profile}

Your goal is not only to determine whether content is safe or dangerous, but also to explain how risky it is for the selected user profile.

Analyze the following content.

CONTENT:
{text}

Use a Threat Correlation Engine:
Instead of analyzing each indicator separately, correlate all available evidence (language patterns, URLs, impersonation attempts, phishing signs, scam tactics, misinformation, social engineering techniques, and suspicious claims) to determine the overall cyber threat level.

Never rely on only one indicator.
Your final verdict must be based on the combined evidence.

Return ONLY the report in markdown.

# 🛡️ AI Cyber Lens Security Report

---

## 🚨 Executive Summary

Summarize the content in 2–3 sentences.

---

## 🎯 Threat Category

Choose all that apply:

- Safe Content
- Scam
- Phishing
- Deepfake
- Fake News
- Impersonation
- Fraud
- Spam
- Malware
- Social Engineering

---

## 🏁 Final Verdict

Choose ONLY one:

🟢 SAFE

🟡 SUSPICIOUS

🔴 DANGEROUS

**Confidence:** XX%

Explain your verdict in 2-3 lines.

---

## ⭐ AI Trust Score

Give a Trust Score out of 100.

Explain the score in one sentence.

---

## 🎯 Personalized Risk Intelligence

**Target Audience:** {user_profile}

**Risk Meter:** XX%

Choose ONLY one:

🟢 LOW RISK

🟡 MEDIUM RISK

🔴 HIGH RISK

Explain why this content is specifically risky (or safe) for the selected user profile.

For example:

Student:
- Fake internships
- Fake scholarships
- Placement scams
- Telegram investment scams
- Fake coding bootcamps

Senior Citizen:
- OTP fraud
- Bank KYC scam
- Lottery scam
- Pension fraud
- Voice cloning

Working Professional:
- Fake HR
- CEO impersonation
- Salary phishing
- Invoice fraud
- Teams/Zoom phishing

Business Owner:
- GST fraud
- Fake vendor
- Invoice manipulation
- Fake payment request
- UPI fraud

Parent:
- School fee scam
- Child emergency scam
- Deepfake voice
- Fake donation

Government Employee:
- Official notice impersonation
- Fake government portal
- Credential phishing
- Email spoofing

Other:
Provide general cyber safety analysis.

---

## 🔗 Threat Correlation Engine

Correlate all detected indicators.

Explain how multiple threats combine to produce the final verdict.

If only one weak indicator exists, mention that the risk is limited.

If several indicators reinforce each other, explain why the overall threat is high.

---

## 🔍 Threat Analysis

| Security Check | Result |
|----------------|--------|
| Scam Indicators | ✅ / ❌ |
| Phishing Signs | ✅ / ❌ |
| Deepfake Risk | High / Medium / Low |
| Fake Information | ✅ / ❌ |
| Suspicious Links | ✅ / ❌ |
| Impersonation | ✅ / ❌ |
| Malware Indicators | ✅ / ❌ |
| Social Engineering | ✅ / ❌ |

---

## ⚠ Key Risk Indicators

List the major warning signs.

If none exist, write:

**No significant threats detected.**

---

## 🛡 Personalized Safety Recommendations

Provide 3–5 recommendations specifically for the selected user profile.

The advice must be practical and tailored to the user's likely cyber risks.

---

## 📚 Official Verification Sources

Return a markdown table.

| Source | Purpose | Official Website |
|--------|---------|------------------|

Recommend ONLY relevant official sources such as:

- CERT-In
- National Cyber Crime Portal
- PIB Fact Check
- Google Safe Browsing
- VirusTotal

Never invent websites or URLs.

---

## 💡 Final Conclusion

Summarize:

- Overall threat level
- Why the AI reached this verdict
- What the selected user should do next

Keep it concise (3–4 lines).

Return ONLY markdown.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.0
    )


    return response.choices[0].message.content


method = st.radio(
    "Choose Analysis Type",
    [
        "📝 Text",
        "🔗 URL",
        "📄 PDF",
        "🖼️ Image"
    ]
)

content = ""

if method == "📝 Text":

    content = st.text_area(
        "Enter text",
        height=220,
        placeholder="Paste any news, message, email, or social media content..."
    )

elif method == "🔗 URL":

    content = st.text_input(
        "Enter website URL",
        placeholder="https://example.com"
    )

elif method == "📄 PDF":

    file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if file:
        content = read_pdf(file)

elif method == "🖼️ Image":

    image = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if image:
        st.image(image, caption="Uploaded Image", use_container_width=True)
        content = "Analyze this image for deepfake signs, scams, manipulation, or misleading content."


if st.button("🔍 Analyze Information"):


    if not api_key:

        st.error(
            "Please enter Groq API Key"
        )


    elif not content:

        st.warning(
            "Please enter text, URL, upload a PDF, or upload an image."
        )


    else:

        with st.spinner(
            "AI Investigator analyzing..."
        ):

            result = analyze(content)



        st.success(
            "Analysis Completed"
        )


    
        st.markdown(result)

if 'result' in locals():
    st.download_button(
        label="📄 Download Report",
        data=result,
        file_name="AI_CyberLens_Report.txt",
        mime="text/plain"
    )

st.divider()

st.caption(
    "AI Cyber Lens | Python + Streamlit + Groq AI"
)