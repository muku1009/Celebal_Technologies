import streamlit as st
import numpy as np
import joblib
import random

# -----------------------------
# 🔹 Load Model and Scaler
# -----------------------------
model = joblib.load("xgboost_spam_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# 🔹 Define Features
# -----------------------------
features = [
    'word_freq_make', 'word_freq_address', 'word_freq_all', 'word_freq_3d',
    'word_freq_our', 'word_freq_over', 'word_freq_remove', 'word_freq_internet',
    'word_freq_order', 'word_freq_mail', 'word_freq_receive', 'word_freq_will',
    'word_freq_people', 'word_freq_report', 'word_freq_addresses', 'word_freq_free',
    'word_freq_business', 'word_freq_email', 'word_freq_you', 'word_freq_credit',
    'word_freq_your', 'word_freq_font', 'word_freq_000', 'word_freq_money',
    'word_freq_hp', 'word_freq_hpl', 'word_freq_george', 'word_freq_650',
    'word_freq_lab', 'word_freq_labs', 'word_freq_telnet', 'word_freq_857', 'word_freq_data',
    'word_freq_415', 'word_freq_85', 'word_freq_technology', 'word_freq_1999',
    'word_freq_parts', 'word_freq_pm', 'word_freq_direct', 'word_freq_cs',
    'word_freq_meeting', 'word_freq_original', 'word_freq_project', 'word_freq_re',
    'word_freq_edu', 'word_freq_table', 'word_freq_conference', 'char_freq_;',
    'char_freq_(', 'char_freq_[', 'char_freq_!', 'char_freq_$', 'char_freq_#',
    'capital_run_length_average', 'capital_run_length_longest', 'capital_run_length_total'
]

# -----------------------------
# 🔹 Default Values (Realistic)
# -----------------------------
default_values = {
    'word_freq_make': 0.21, 'word_freq_address': 0.06, 'word_freq_all': 0.42, 'word_freq_3d': 0.01,
    'word_freq_our': 0.51, 'word_freq_over': 0.14, 'word_freq_remove': 0.36, 'word_freq_internet': 0.10,
    'word_freq_order': 0.55, 'word_freq_mail': 0.20, 'word_freq_receive': 0.18, 'word_freq_will': 0.37,
    'word_freq_people': 0.04, 'word_freq_report': 0.02, 'word_freq_addresses': 0.01, 'word_freq_free': 0.75,
    'word_freq_business': 0.45, 'word_freq_email': 0.60, 'word_freq_you': 0.67, 'word_freq_credit': 0.31,
    'word_freq_your': 0.90, 'word_freq_font': 0.08, 'word_freq_000': 0.25, 'word_freq_money': 0.28,
    'word_freq_hp': 0.02, 'word_freq_hpl': 0.01, 'word_freq_george': 0.01, 'word_freq_650': 0.01,
    'word_freq_lab': 0.02, 'word_freq_labs': 0.02, 'word_freq_telnet': 0.00, 'word_freq_857': 0.00, 'word_freq_data': 0.06,
    'word_freq_415': 0.01, 'word_freq_85': 0.03, 'word_freq_technology': 0.02, 'word_freq_1999': 0.04,
    'word_freq_parts': 0.01, 'word_freq_pm': 0.01, 'word_freq_direct': 0.04, 'word_freq_cs': 0.02,
    'word_freq_meeting': 0.03, 'word_freq_original': 0.03, 'word_freq_project': 0.02, 'word_freq_re': 0.08,
    'word_freq_edu': 0.02, 'word_freq_table': 0.01, 'word_freq_conference': 0.02, 'char_freq_;': 0.05,
    'char_freq_(': 0.10, 'char_freq_[': 0.03, 'char_freq_!': 0.60, 'char_freq_$': 0.48, 'char_freq_#': 0.06,
    'capital_run_length_average': 3.5, 'capital_run_length_longest': 40, 'capital_run_length_total': 80
}

# -----------------------------
# 🔹 Random Input Generator
# -----------------------------
def get_random_input():
    random_input = {f: round(random.uniform(0, 1), 2) for f in features}
    random_input['capital_run_length_average'] = round(random.uniform(1, 10), 2)
    random_input['capital_run_length_longest'] = random.randint(10, 100)
    random_input['capital_run_length_total'] = random.randint(50, 300)
    return random_input

# -----------------------------
# 🔹 Streamlit UI
# -----------------------------
st.set_page_config(page_title="Spam Classifier", layout="wide")
st.title("📧 Spam Email Classifier")
st.write("Enter email feature values below to classify it as **Spam** or **Not Spam**.")

# Init session state
if 'inputs' not in st.session_state:
    st.session_state.inputs = default_values.copy()

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🔁 Autofill Random Values"):
        st.session_state.inputs = get_random_input()

with col2:
    if st.button("♻️ Reset to Defaults"):
        st.session_state.inputs = default_values.copy()

# Collect input
user_input = []
st.markdown("---")
for feature in features:
    if feature in ['capital_run_length_longest', 'capital_run_length_total']:
        val = st.number_input(
            f"{feature}",
            value=int(st.session_state.inputs.get(feature, 0)),
            min_value=0,
            step=1,
            format="%d",
            key=feature
        )
    else:
        val = st.number_input(
            f"{feature}",
            value=float(st.session_state.inputs.get(feature, 0.0)),
            min_value=0.0,
            step=0.001,
            format="%.3f",
            key=feature
        )
    user_input.append(val)



# -----------------------------
# 🔹 Prediction
# -----------------------------
if st.button("🚀 Predict"):
    input_array = np.array(user_input).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    proba = model.predict_proba(input_scaled)[0][1]

    st.markdown("---")
    if prediction == 1:
        st.error(f"🚨 This email is classified as **SPAM**.")
    else:
        st.success(f"✅ This email is classified as **NOT SPAM**.")

    st.info(f"📊 Spam Probability: **{proba:.2%}**")

