import streamlit as st

st.set_page_config(page_title="Stress Detection System", layout="centered")

st.title("Smartphone-Based Stress Detection System")

st.subheader("Relaxation Preference")

relaxation_method = st.selectbox(
    "How do you usually relax when stressed?",
    [
        "Deep Breathing",
        "Listening to Music",
        "Tea / Coffee",
        "Walking",
        "Meditation",
        "Sleeping",
        "Other"
    ]
)

custom_relaxation = None
if relaxation_method == "Other":
    custom_relaxation = st.text_input(
        "Please specify your relaxation method"
    )

# Stop here until relaxation method is chosen properly
if relaxation_method == "Other" and not custom_relaxation:
    st.warning("Please enter your relaxation method to continue.")
    st.stop()

# Final relaxation choice
final_relaxation = custom_relaxation if relaxation_method == "Other" else relaxation_method

st.divider()

st.subheader("Enter Health & Activity Details")

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=40,
    max_value=200,
    value=75
)

temperature = st.number_input(
    "Body Temperature (°C)",
    min_value=35.0,
    max_value=110.0,
    value=36.8
)

activity = st.selectbox(
    "Current Activity",
    ["Walking", "Standing", "Sitting", "Sleeping"]
)

sleep_hours = st.slider(
    "Sleep Duration (hours)",
    0.0, 12.0, 7.0
)

screen_time = st.slider(
    "Screen Time (hours/day)",
    0.0, 24.0, 5.0
)

stress = "Low"
reasons = []


if heart_rate >= 100:
    stress = "High"
    reasons.append("Very high heart rate")

if temperature >= 38:
    stress = "High"
    reasons.append("Very high body temperature")

if sleep_hours < 4:
    stress = "High"
    reasons.append("Severe sleep deprivation")

if screen_time >= 10:
    stress = "High"
    reasons.append("Excessive screen time")

# MEDIUM stress (only if not HIGH)
if stress != "High":
    if activity in ["Sitting", "Standing"]:
        stress = "Medium"
        reasons.append("Low physical movement")

    if sleep_hours < 6:
        stress = "Medium"
        reasons.append("Insufficient sleep")

# LOW stress explanation
if stress == "Low":
    reasons.append("Healthy activity and normal vitals")


st.divider()

if st.button("Predict Stress Level"):
    st.subheader("Stress Assessment Result")

    if stress == "Low":
        st.success("Stress Level: LOW")
    elif stress == "Medium":
        st.warning("Stress Level: MEDIUM")
    else:
        st.error("Stress Level: HIGH")

    st.write("### Reasons:")
    for r in reasons:
        st.write(f"- {r}")


    if stress == "High":
        st.subheader("Personalized Relaxation Suggestion")
        st.info(f"We recommend you try: **{final_relaxation}**")
