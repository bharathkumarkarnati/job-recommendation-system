import os
import joblib
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# LOAD MODEL AND DATA
# =========================================================
model = joblib.load("random_forest_model.pkl")
skill_columns = joblib.load("skill_columns.pkl")
df = pd.read_csv("dataset/job_profiles_cleaned.csv")

st.set_page_config(page_title="Job Recommendation System", layout="wide")

# Hide Streamlit chrome so only our UI shows
st.markdown("""
<style>
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.stApp { background-color: #f7f9fa; }
.block-container { max-width: 100% !important; padding: 0 !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# COMPONENT (loads frontend/index.html)
# =========================================================
_dir = os.path.dirname(os.path.abspath(__file__))
job_ui = components.declare_component("job_ui", path=os.path.join(_dir, "frontend"))


# =========================================================
# HELPERS
# =========================================================
def get_required_skills(role):
    role_data = df[df["Job_Role"] == role]
    skill_frequency = role_data[skill_columns].mean()
    return skill_frequency[skill_frequency >= 0.50].sort_values(
        ascending=False
    ).index.tolist()


def predict(selected_skills):
    """ML model prediction -> top 5 roles with match details."""
    user_input = pd.DataFrame(0, index=[0], columns=skill_columns)
    for skill in selected_skills:
        if skill in skill_columns:
            user_input[skill] = 1

    probabilities = model.predict_proba(user_input)[0]
    recs = pd.DataFrame({
        "Job Role": model.classes_,
        "Confidence": probabilities * 100,
    }).sort_values("Confidence", ascending=False).head(5)

    items = []
    for _, row in recs.iterrows():
        role = str(row["Job Role"])
        required = get_required_skills(role)
        matching = [s for s in required if s in selected_skills]
        missing = [s for s in required if s not in selected_skills]
        match = (len(matching) / len(required) * 100) if required else 0
        items.append({
            "role": role,
            "match": float(match),
            "matching": matching,
            "missing": missing,
        })
    return items


# =========================================================
# SESSION STATE
# =========================================================
if "result" not in st.session_state:
    st.session_state.result = None
if "last_nonce" not in st.session_state:
    st.session_state.last_nonce = None

roles = sorted(str(r) for r in df["Job_Role"].unique())
required_by_role = {r: get_required_skills(r) for r in roles}

# =========================================================
# RENDER UI
# =========================================================
value = job_ui(
    roles=roles,
    required=required_by_role,
    result=st.session_state.result,
    key="job_ui",
    default=None,
)

# UI asked for a prediction -> run the ML model, then rerun to send result back
if value and value.get("action") == "predict" and value.get("nonce") != st.session_state.last_nonce:
    st.session_state.result = {
        "nonce": value["nonce"],
        "items": predict(value.get("skills", [])),
    }
    st.session_state.last_nonce = value["nonce"]
    st.rerun()