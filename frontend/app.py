import streamlit as st
import requests
import os
import pandas as pd
from datetime import datetime

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="EduTrack Pro - Student Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Hide Streamlit Defaults ---
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Colorful 3D Neon Border Design ---
st.markdown("""
<style>

@keyframes borderGlow {
  0% { border-image-source: linear-gradient(0deg, #00ffff, #ff00ff, #ff9900, #00ffff); }
  50% { border-image-source: linear-gradient(180deg, #ff00ff, #00ffff, #ff9900, #ff00ff); }
  100% { border-image-source: linear-gradient(360deg, #00ffff, #ff00ff, #ff9900, #00ffff); }
}

@keyframes backgroundShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.stApp {
  background: linear-gradient(-45deg, #0f0c29, #302b63, #a855f7, #00c6ff, #ff00cc);
  background-size: 400% 400%;
  animation: backgroundShift 10s ease infinite;
  color: #fff;
  font-family: 'Poppins', sans-serif;
}

/* 3D Glowing Hero Header with Animated Border */
.hero-header {
  position: relative;
  text-align: center;
  border: 6px solid transparent;
  border-radius: 35px;
  border-image-slice: 1;
  animation: borderGlow 6s linear infinite;
  padding: 60px 40px;
  margin-bottom: 50px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  backdrop-filter: blur(15px);
  background: rgba(255,255,255,0.05);
}
.hero-header h1 {
  font-size: 60px;
  font-weight: 900;
  background: linear-gradient(135deg, #ff00cc, #3333ff, #00ffff, #ff9900);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 0 30px rgba(168,85,247,0.8);
}
.hero-header p {
  color: #e0e0e0;
  font-size: 22px;
  text-shadow: 0 0 12px rgba(0,0,0,0.6);
}
.hero-subtitle {
  color: #c084fc;
  font-size: 18px;
}

/* Glowing Info & Feature Cards */
.info-card, .feature-card {
  background: rgba(255,255,255,0.07);
  border: 3px solid transparent;
  border-image: linear-gradient(135deg, #ff00ff, #00ffff, #ffcc00, #ff00ff);
  border-image-slice: 1;
  border-radius: 20px;
  padding: 25px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.4), 0 0 20px rgba(168,85,247,0.4);
  transition: all 0.4s ease;
}
.info-card:hover, .feature-card:hover {
  transform: translateY(-10px) scale(1.03);
  box-shadow: 0 12px 40px rgba(255,255,255,0.3), 0 0 25px rgba(0,255,255,0.6);
}

/* Fancy Gradient Buttons */
.stButton>button {
  background: linear-gradient(135deg, #00ffff, #7b2ff7, #f72585, #ffcc00);
  color: white;
  border: 2px solid transparent;
  border-image: linear-gradient(135deg, #00ffff, #f72585, #ffcc00);
  border-image-slice: 1;
  border-radius: 18px;
  font-size: 18px;
  font-weight: 700;
  padding: 14px 28px;
  box-shadow: 0 6px 25px rgba(255,255,255,0.3);
  transition: all 0.3s ease;
}
.stButton>button:hover {
  transform: scale(1.08);
  box-shadow: 0 0 40px rgba(255,0,255,0.8), 0 0 20px rgba(0,255,255,0.8);
}

/* Input fields with glow */
.stTextInput>div>div>input, .stNumberInput>div>div>input {
  background: rgba(255,255,255,0.08);
  border: 2px solid transparent;
  border-image: linear-gradient(135deg, #00ffff, #f72585, #ffcc00);
  border-image-slice: 1;
  border-radius: 12px;
  color: #00e5ff;
  font-size: 16px;
  padding: 14px;
}
.stTextInput>div>div>input:focus {
  border-color: #a855f7;
  box-shadow: 0 0 20px rgba(168,85,247,0.6);
}

/* Section Header */
.section-header {
  font-size: 36px;
  font-weight: 800;
  color: #fff;
  text-shadow: 0 0 25px rgba(168,85,247,0.8);
  margin-bottom: 25px;
  border-bottom: 3px solid;
  border-image: linear-gradient(135deg, #ff00ff, #00ffff, #ffcc00);
  border-image-slice: 1;
}

/* Footer */
.footer {
  text-align: center;
  padding: 30px;
  margin-top: 40px;
  border-radius: 20px;
  border: 3px solid transparent;
  border-image: linear-gradient(135deg, #00ffff, #a855f7, #ff00cc);
  border-image-slice: 1;
  background: rgba(255,255,255,0.05);
  color: #d1c4e9;
  box-shadow: 0 5px 30px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)

# --- Hero Header ---
current_time = datetime.now().strftime("%B %d, %Y")
st.markdown(f"""
<div class="hero-header">
    <h1>🎓 Multicloud DevOps by AvinashRaju</h1>
    <p>Next-Gen Student Management & Analytics Platform</p>
    <div class="hero-subtitle">📅 {current_time} | 🌐 Powered by Spring Boot & Streamlit</div>
</div>
""", unsafe_allow_html=True)

# --- API URL ---
API_URL = os.environ.get("API_URL", "http://localhost:8081")

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Student", "🔍 Search Student", "📋 All Students", "📊 Analytics"])

# --- TAB 1 ---
with tab1:
    st.markdown('<div class="section-header">➕ Register New Student</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3,2])
    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>📝 Student Registration Form</h3>
            <p>Enter details below to add a new student record.</p>
        </div>
        """, unsafe_allow_html=True)
        with st.form("add_student_form", clear_on_submit=True):
            name = st.text_input("👤 Student Full Name", placeholder="e.g., John Doe")
            age = st.number_input("🎂 Age", min_value=1, max_value=100, value=18)
            submit = st.form_submit_button("🚀 Add Student")
            if submit:
                if name:
                    try:
                        r = requests.post(f"{API_URL}/student/post", json={"name": name, "age": age})
                        if r.status_code == 200:
                            st.success(f"✅ Student '{name}' added successfully!")
                            st.balloons()
                        else:
                            st.error(f"❌ Error: {r.text}")
                    except Exception as e:
                        st.error(f"🔌 Backend Error: {e}")
                else:
                    st.warning("⚠️ Please enter a name.")
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>💡 Tips</h4>
            <p>• Use unique names<br>• Verify details<br>• Refresh the list to confirm data</p>
        </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown(f"""
<div class="footer">
🎓 <b>EduTrack Pro</b> — Colorful Neon 3D Dashboard by <b>AvinashRaju</b><br>
💻 Built with ❤️ using Streamlit + Spring Boot | © 2025
</div>
""", unsafe_allow_html=True)
                
