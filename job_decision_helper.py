# job_decision_helper.py
import streamlit as st

st.title("Should I Change Jobs Right Now?")

st.write("Answer honestly. This tool is about clarity, not motivation.")

score = 0

# Financial Safety
months_saved = st.selectbox(
    "How many months of living expenses do you have saved?",
    ["0–1", "2–3", "4–5", "6+"]
)
score += {"0–1": 2, "2–3": 8, "4–5": 15, "6+": 25}[months_saved]

income_stability = st.slider("How stable is your current income?", 0, 10)
score += income_stability * 1.5

dependents = st.radio("Do others depend on your income?", ["Yes", "No"])
score += 0 if dependents == "Yes" else 5

# Job Health
stress = st.slider("How stressed are you at work most days?", 0, 10)
score += (10 - stress) * 2.5

growth = st.selectbox(
    "Are you learning skills that increase your future value?",
    ["No", "Somewhat", "Yes"]
)
score += {"No": 5, "Somewhat": 12, "Yes": 25}[growth]

# Opportunity Quality
pay = st.selectbox(
    "Does the new opportunity increase total compensation?",
    ["No", "Slightly", "Significantly"]
)
score += {"No": 0, "Slightly": 10, "Significantly": 20}[pay]

clarity = st.selectbox(
    "Is the role clearly defined with realistic expectations?",
    ["No", "Somewhat", "Yes"]
)
score += {"No": 0, "Somewhat": 10, "Yes": 20}[clarity]

# Personal Readiness
energy = st.slider(
    "How much energy do you have outside of work to job search?",
    0, 10
)
score += energy * 2

confidence = st.slider(
    "How confident are you you could find another role within 3 months?",
    0, 10
)
score += confidence * 2

st.write(f"### Your score: {int(score)} / 100")

if score < 40:
    st.error("Recommendation: **Stay for now**")
    st.write("Focus on stabilizing finances and reducing stress.")
elif score < 70:
    st.warning("Recommendation: **Prepare to leave**")
    st.write("Line up savings, update your resume, and start networking.")
else:
    st.success("Recommendation: **Leave now**")
    st.write("Your financial safety and readiness are strong.")

st.caption("This tool provides structured thinking, not life advice.")
