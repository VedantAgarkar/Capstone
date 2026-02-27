import streamlit as st
import time
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path for importing utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_common_styling, render_navbar, get_openai_client, get_model_name, call_openai_api, get_language

# Load environment variables
load_dotenv()

# Get current language
LANG = get_language()

# ─────────────── Localization Dictionary for Triage Bot ─────────────── #
LABELS = {
    "en": {
        "title": "AI Symptom Checker (Triage)",
        "hello": "👋 Welcome to the Triage Center. Please describe your symptoms in detail, and I will guide you to the most appropriate medical assessment or suggest immediate care if needed.",
        "placeholder": "Describe your symptoms (e.g., 'I have chest pain and shortness of breath' or 'I feel shaky')...",
        "thinking": "🤖💬 Analyzing symptoms...",
        "error": "❌ Analysis failed. Please try again.",
        "system_prompt": """You are an AI Medical Triage Assistant for the HealthPredict platform.
Your goal is to analyze user symptoms and recommend one of the following assessments:
1. Heart Disease Assessment (for chest pain, breathlessness, irregular heartbeat)
2. Diabetes Risk Assessment (for frequent thirst, fatigue, blurred vision, slow-healing wounds)
3. Parkinson's Disease Assessment (for tremors, stiffness, slow movement, voice changes)

If symptoms are severe (e.g., severe chest pain, stroke signs), recommend IMMEDIATE EMERGENCY CARE.

RESPONSE FORMAT:
- Acknowledge symptoms.
- Map them to the specific risk assessment above.
- Provide a clear recommendation.
- ALWAYS include the specific links:
  - Heart: http://localhost:8501
  - Diabetes: http://localhost:8502
  - Parkinson's: http://localhost:8503

IMPORTANT: Remind the user you are an AI, not a doctor.
""",
        "nav_title": " HealthPredict",
        "footer": "HealthPredict | AI Symptom Checker"
    },
    "mr": {
        "title": "एआय लक्षण तपासणी (Triage)",
        "hello": "👋 ट्रायज सेंटरमध्ये आपले स्वागत आहे. कृपया तुमच्या लक्षणांचे तपशीलवार वर्णन करा आणि मी तुम्हाला योग्य वैद्यकीय मूल्यमापनासाठी मार्गदर्शन करेन किंवा गरज भासल्यास त्वरित उपचारांची सूचना देईन.",
        "placeholder": "तुमच्या लक्षणांचे वर्णन करा (उदा. 'माझ्या छातीत दुखत आहे आणि श्वास घेण्यास त्रास होत आहे' किंवा 'मला थरथरणार असल्यासारखे वाटते')...",
        "thinking": "🤖💬 लक्षणांचे विश्लेषण करत आहे...",
        "error": "❌ विश्लेषण अयशस्वी. कृपया पुन्हा प्रयत्न करा.",
        "system_prompt": """तुम्ही HealthPredict प्लॅटफॉर्मसाठी एआय मेडिकल ट्रायज असिस्टंट आहात.
तुमचे उद्दिष्ट वापरकर्त्याच्या लक्षणांचे विश्लेषण करणे आणि खालीलपैकी एका मूल्यांकनाची शिफारस करणे आहे:
1. हृदय रोग मूल्यांकन (छातीत दुखणे, धाप लागणे, अनियमित हृदयाचे ठोके यासाठी)
2. मधुमेह जोखीम मूल्यांकन (वारंवार तहान लागणे, थकवा, अंधुक दृष्टी, सावकाश भरणारी जखम यासाठी)
3. पार्किन्सन रोग मूल्यांकन (थरथर, कडकपणा, संथ हालचाल, आवाजातील बदल यासाठी)

जर लक्षणे गंभीर असतील (उदा. तीव्र छातीत दुखणे, स्ट्रोकची चिन्हे), तर त्वरित आपत्कालीन उपचारांची शिफारस करा.

प्रतिसाद स्वरूप:
- लक्षणांची नोंद घ्या.
- वर नमूद केलेल्या विशिष्ट जोखीम मूल्यांकनाशी त्यांना जोडा.
- स्पष्ट शिफारस द्या.
- नेहमी खालील दुवे समाविष्ट करा:
  - हृदय (Heart): http://localhost:8501
  - मधुमेह (Diabetes): http://localhost:8502
  - पार्किन्सन (Parkinson's): http://localhost:8503

महत्त्वाचे: वापरकर्त्याला आठवण करून द्या की तुम्ही एआय आहात, डॉक्टर नाही. प्रतिसाद मराठीत द्या.
""",
        "nav_title": " HealthPredict",
        "footer": "HealthPredict | एआय लक्षण तपासणी"
    }
}

def L(key):
    return LABELS.get(LANG, LABELS["en"]).get(key, key)

# ───── Streamlit Config ───── #
st.set_page_config(layout="wide", page_title=f"HealthPredict - {L('title')}")

# ───────────────🔐 API Setup ─────────────── #
try:
    client = get_openai_client()
    openrouter_model = get_model_name()
except ValueError as e:
    st.error(f"Configuration Error: {str(e)}. Please set OPENROUTER_API_KEY in environment.")
    st.stop()

# ───── Hide Streamlit Default Elements & Apply Styling ───── #
apply_common_styling()

st.markdown("""
<style>
.nav-link {
    color: white !important;
    text-decoration: none !important;
    transition: color 0.3s ease;
}
.nav-link:hover {
    color: #B79347 !important;
}
.triage-card {
    background: rgba(183, 147, 71, 0.1);
    border: 1px solid #B79347;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# ───── Navbar ───── #
render_navbar(L('nav_title'))

# ───── Title ───── #
st.title(L('title'))
st.write(L('hello'))

# ───── Chat State Setup ───── #
if "triage_messages" not in st.session_state:
    st.session_state.triage_messages = []

# ───── Show All Previous Messages ───── #
for msg in st.session_state.triage_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ───── User Chat Input ───── #
if user_input := st.chat_input(L('placeholder')):
    st.session_state.triage_messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner(L('thinking')):
            system_prompt = L('system_prompt')
            
            full_response = call_openai_api(client, user_input, openrouter_model, timeout=30, system_prompt=system_prompt)
            
            if full_response:
                # Simulate typing effect
                display_text = ""
                for word in full_response.split():
                    display_text += word + " "
                    time.sleep(0.03)
                    message_placeholder.markdown(display_text + "▌")
                message_placeholder.markdown(full_response)
            else:
                error_msg = L('error')
                message_placeholder.error(error_msg)
                full_response = error_msg
        
        # LOG INTERACTION TO DATABASE
        try:
            from database import log_prediction
            from utils import get_email
            email = get_email()
            log_prediction(email, "Triage Bot", user_input, "Triage Suggestion Provided")
        except Exception as log_err:
            pass

    st.session_state.triage_messages.append({"role": "assistant", "content": full_response})

# ───── Assessment Quick Links ───── #
st.sidebar.markdown("### Quick Access")
st.sidebar.markdown(f"- [❤️ Heart Assessment](http://localhost:8501?lang={LANG})")
st.sidebar.markdown(f"- [🩸 Diabetes Assessment](http://localhost:8502?lang={LANG})")
st.sidebar.markdown(f"- [🧠 Parkinson's Assessment](http://localhost:8503?lang={LANG})")

# ───── Sticky Footer ───── #
st.markdown(f"""
<style>
.footer {{
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #06061C;
    color: gold;
    text-align: center;
    padding: 15px 0;
    font-size: 14px;
    z-index: 9999;
}}
</style>
<div class="footer">
    &copy; 2026 {L('footer')}
</div>
""", unsafe_allow_html=True)
