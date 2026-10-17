import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="IBM Z - Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# Title & Infrastructure Info
st.title("🛡️ Smart Real-Time Fraud Detection Dashboard")
st.caption("Hosted on IBM Z / LinuxONE Community Cloud (Ubuntu 24.04)")

# Sidebar Configuration
st.sidebar.header("Control Panel")
risk_threshold = st.sidebar.slider("Set Risk Score Threshold (%)", 0, 100, 75)

# Metrics Display
st.subheader("📊 Real-Time Transaction Stream Analysis")

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions Monitored", "1,248", "+12/min")
col2.metric("Flagged Fraud Risk", "3", "-1", delta_color="inverse")
col3.metric("LinuxONE System Health", "100% Active", "Normal")

st.write("---")

# Sample Data
data = {
    "Transaction ID": ["TXN-9021", "TXN-9022", "TXN-9023", "TXN-9024"],
    "User ID": ["USR-102", "USR-405", "USR-881", "USR-309"],
    "Amount ($)": [120.50, 4500.00, 15.25, 8900.00],
    "Calculated Risk Score (%)": [12, 88, 5, 94],
    "Status": ["Safe", "High Risk Flag", "Safe", "Critical Fraud Alert"]
}

df = pd.DataFrame(data)

def highlight_risk(val):
    color = '#ff4b4b' if val >= risk_threshold else '#21c354'
    return f'background-color: {color}; color: white; font-weight: bold;'

st.dataframe(df.style.applymap(highlight_risk, subset=['Calculated Risk Score (%)']), use_container_width=True)
st.success("✅ Analytics engine running stably on IBM Z LinuxONE instance (SoloCoderVM).")
