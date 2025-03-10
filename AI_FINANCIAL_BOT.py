import streamlit as st
import openai

# Set OpenAI API key (Replace with your key)
openai.api_key = "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"

# Loan Estimator Function
def get_loan_recommendation(income, credit_score, purchase_amount):
    if credit_score >= 700:
        return "✅ You're eligible for Snap Finance’s premium loan plan with lower interest rates!"
    elif credit_score >= 600:
        return "✅ You qualify for a standard financing plan."
    else:
        return "⚠️ Approval might be difficult, but you can try a co-signer."

# AI Chatbot Function
def chat_with_ai(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful financial assistant."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

# Fraud Detection Logic
suspicious_users = {}
def detect_fraud(user_id, query):
    if user_id in suspicious_users:
        suspicious_users[user_id] += 1
    else:
        suspicious_users[user_id] = 1

    if suspicious_users[user_id] > 3:
        return "⚠️ Warning: Multiple inconsistent financing requests detected!"
    return "✅ Request processed successfully."

# Streamlit UI
st.title("💰 AI Finance Assistant")

# User Query Input
user_input = st.text_input("Ask me about Snap Finance & Loan Options:")
if st.button("Submit Query"):
    st.write("🤖", chat_with_ai(user_input))

# Loan Estimator Form
st.subheader("📊 Loan Pre-Approval Estimator")
income = st.number_input("Monthly Income ($)", min_value=0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850)
purchase_amount = st.number_input("Purchase Amount ($)", min_value=0)
if st.button("Check Eligibility"):
    st.write(get_loan_recommendation(income, credit_score, purchase_amount))

# Fraud Detection
user_id = "demo_user"  # Replace with actual user ID in production
if st.button("Detect Fraud Attempts"):
    st.write(detect_fraud(user_id, user_input))

# Voice Input Feature
if st.button("Use Voice Input 🎤"):
    st.write("🗣️ You said:", voice_text)
    st.write("🤖 AI Response:", chat_with_ai(voice_text))