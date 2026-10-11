import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="UPI Safety Coach Chatbot", page_icon="🛡️", layout="centered"
)

# Custom Styling for Clean Chat UI
st.markdown(
    """
    <style>
    .main {background-color: #f4f6f9;}
    .stAlert {border-radius: 10px;}
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.title("🛡️ UPI Safety Coach Chatbot")
st.markdown(
    "*Your personal AI assistant to detect digital payment scams before you lose money.*[cite: 4]"
)

# Sidebar - Project Details & Disclaimers
with st.sidebar:
    st.header("📌 Project Details")
    st.markdown("**Target:** Grade 9 AI Revolution & Digital Futures[cite: 1]")
    st.markdown("**Platform:** Python & Streamlit Prototype")

    st.markdown("---")
    st.error(
        "⚠️ **SAFETY REMINDER**\nNever type your real UPI PIN, OTP, or bank passwords into any chatbot!"
    )

    st.markdown("---")
    st.markdown("🚨 **Emergency Helpline:**")
    st.markdown("**National Cyber Helpline:** `1930`[cite: 2, 4]")
    st.markdown("**Portal:** [cybercrime.gov.in](https://cybercrime.gov.in)")

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "Hello! I am your **UPI Safety Coach**. "
            "Did someone send you a suspicious link, ask for an OTP, or give you a strange QR code? "
            "Describe your situation below or pick a quick test scenario!"
        ),
    }]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Intelligent Scam Analysis Function (5 Scenarios)
def analyze_scam(user_input):
    text = user_input.lower()

    # Scenario 1: QR Code Trap (Receive Money Scam)
    if any(
        word in text
        for word in [
            "qr",
            "scan",
            "receive money",
            "cashback",
            "olx buyer",
            "sell",
        ]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (QR Code Payment Trap)**[cite: 5]\n\n"
            "🔍 **Why it's a scam:** QR codes are **strictly for sending money**, never for receiving funds[cite: 5, 8]. Scanning a QR code and entering your UPI PIN will always deduct money from your account[cite: 8].\n\n"
            "🛡️ **What you should do:**\n"
            "1. Cancel the transaction immediately. Do not scan or enter your PIN[cite: 5].\n"
            "2. Block the user on the marketplace platform.\n"
            "3. If money was deducted, report immediately to **1930** or [cybercrime.gov.in](https://cybercrime.gov.in)[cite: 2, 4]."
        )

    # Scenario 2: OTP / PIN Phishing (Fake Bank/KYC)
    elif any(
        word in text for word in ["otp", "pin", "bank call", "block", "kyc"]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (OTP / PIN Phishing Scam)**[cite: 5]\n\n"
            "🔍 **Why it's a scam:** Banks, RBI, and UPI apps **never** ask for your OTP, UPI PIN, or password over a call or message[cite: 2, 4, 8].\n\n"
            "🛡️ **What you should do:**\n"
            "1. Hang up the phone instantly. Never share your OTP (*'OTP is Only To Yourself'*)[cite: 7, 8].\n"
            "2. Block the caller's number.\n"
            "3. If you shared your PIN, change your UPI PIN immediately through your official payment app."
        )

    # Scenario 3: Screen Sharing App Scam (Remote Access)
    elif any(
        word in text
        for word in [
            "anydesk",
            "teamviewer",
            "screen share",
            "remote",
            "quicksupport",
        ]
    ):
        return (
            "🛑 **VERDICT: CRITICAL RISK (Remote Access Fraud)**[cite: 5]\n\n"
            "🔍 **Why it's a scam:** Screen-sharing apps allow fraudsters to view your live phone screen, access your banking apps, and steal money directly[cite: 5, 8].\n\n"
            "🛡️ **What you should do:**\n"
            "1. Do **not** install any remote access app[cite: 5, 8].\n"
            "2. If already installed, disconnect your internet immediately, uninstall the app, and secure your phone.\n"
            "3. Call **1930** right away[cite: 2, 4]."
        )

    # Scenario 4: Fake Customer Care Impersonation
    elif any(
        word in text
        for word in ["customer care", "support", "google search", "helpline"]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (Fake Customer Care Impersonation)**[cite: 5]\n\n"
            "🔍 **Why it's a scam:** Scammers buy sponsored search engine ads to display fake helpline numbers. Legitimate support never asks for a 'verification fee' to process a refund[cite: 8].\n\n"
            "🛡️ **What you should do:**\n"
            "1. Disconnect the call immediately.\n"
            "2. Only look for customer support inside the official help section of verified apps (e.g., Zomato, Paytm, GPay)[cite: 5, 8].\n"
            "3. Report fraudulent numbers to cybercrime authorities[cite: 2, 4]."
        )

    # Scenario 5: AI Deepfake Voice Scam
    elif any(
        word in text
        for word in ["voice", "accident", "emergency", "family", "deepfake"]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (AI Deepfake / Emergency Fraud)**[cite: 5]\n\n"
            "🔍 **Why it's a scam:** Fraudsters use AI audio cloning tools to replicate family members' voices using short clips from social media to create fake emergencies[cite: 5, 8].\n\n"
            "🛡️ **What you should do:**\n"
            "1. Stay calm and hang up[cite: 5, 8].\n"
            "2. Cross-verify by calling your family member back directly on their standard phone number before sending money[cite: 5, 8].\n"
            "3. Report suspicious voice scam attempts to **1930**[cite: 2, 4]."
        )

    # Fallback response for unlisted queries
    else:
        return (
            "⚠️ **UNRECOGNIZED SITUATION**\n\n"
            "I couldn't match your exact situation, but remember the golden rule: **Never share your OTP/PIN, never scan QR codes to receive money, and never install remote-sharing apps[cite: 2, 5, 8].**\n\n"
            "If you suspect financial fraud, call the National Cyber Crime Helpline at **1930** or visit [cybercrime.gov.in](https://cybercrime.gov.in)[cite: 2, 4]."
        )


# Quick-Test Scenario Buttons
st.markdown("### ⚡ Test Core Scenarios")
col1, col2, col3 = st.columns(3)

trigger_input = None
if col1.button("📷 QR Code Trap"):
    trigger_input = "Someone sent me a QR code to receive money."
if col2.button("🔑 OTP / KYC Call"):
    trigger_input = "A caller said my account will be blocked unless I give my OTP."
if col3.button("💻 Screen Share"):
    trigger_input = "Customer care asked me to download AnyDesk for a refund."

col4, col5 = st.columns(2)
if col4.button("🎧 Fake Support"):
    trigger_input = "I called a support number from Google and they asked for a fee."
if col5.button("🗣️ AI Voice Scam"):
    trigger_input = (
        "I got an urgent call sounding like a relative asking for money."
    )

# Chat Input Box
user_query = st.chat_input(
    "Type your suspicious situation here (e.g., 'Someone asked for my OTP')..."
)

if trigger_input:
    user_query = trigger_input

if user_query:
    # Save & display user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate & display assistant response
    bot_reply = analyze_scam(user_query)
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
