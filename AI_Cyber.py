import streamlit as st
from groq import Groq
from pypdf import PdfReader


st.set_page_config(
    page_title="AI Cyber Lens",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI Cyber Lens")

st.subheader("Detect Deepfakes, Scams & Digital Threats with AI")

st.write(
    "An AI-powered cybersecurity platform that analyzes text, URLs, PDFs, and images to detect deepfakes, phishing, scams, fake news, and other digital threats."
)

api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)



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
You are AI Cyber Lens, an expert cybersecurity assistant that detects deepfakes, scams, phishing, fake news, impersonation, and digital fraud.

Analyze the following content.

CONTENT:
{text}

Return ONLY the report in markdown.

# 🛡️ TruthLens Security Report

## 🚨 Executive Summary
Summarize the content in 2–3 sentences.

---

## 🎯 Threat Category

Choose all that apply:

- Safe Content
- Deepfake
- Scam
- Phishing
- Fake News
- Impersonation
- Fraud
- Spam

---

## 🏁 Verdict

Choose ONLY one:

🟢 SAFE

🟡 SUSPICIOUS

🔴 DANGEROUS

**Confidence:** XX%

Give a brief reason.

---

## ⭐ AI Trust Score

Give a score out of **100** with one-line justification.

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

---

## ⚠ Key Risk Indicators

List the main warning signs.

If none are found, write:

**No significant threats detected.**

---

## 🛡 Safety Recommendations

Provide 3–5 practical recommendations.

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

Write a concise 3–4 line conclusion explaining the verdict and what the user should do next.

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