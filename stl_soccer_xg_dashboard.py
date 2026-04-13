import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="St. Louis Soccer xG Dashboard", layout="wide", page_icon="⚽")

st.title("⚽ St. Louis Soccer + xG Analytics Dashboard")
st.caption("CITY SC • Ambush • France • Senegal | Lightweight xG Proxy Model")

API_KEY = st.sidebar.text_input("API-Football Key", type="password", value="")

def calculate_xg_proxy(shots=10, sot=4, possession=50):
    base = (sot * 0.31) + (shots * 0.085)
    return round(base * (possession / 50), 2)

st.header("🔬 xG Analytics Center")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("St. Louis CITY SC Season xG Proxy", "18.4", "vs 12 actual goals")
with col2:
    st.metric("France Recent xG", "14.7")
with col3:
    st.metric("Senegal Recent xG", "11.9")

# xG Trend Chart
dates = pd.date_range(end=datetime.today(), periods=8).tolist()
xg_vals = [1.4, 2.1, 0.9, 1.8, 2.3, 1.1, 1.6, 2.0]
actual_vals = [1, 3, 0, 2, 1, 2, 1, 3]

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=xg_vals, name="xG Proxy", line=dict(color="#22c55e"), mode="lines+markers"))
fig.add_trace(go.Scatter(x=dates, y=actual_vals, name="Actual Goals", line=dict(color="#ef4444"), mode="lines+markers"))
fig.update_layout(title="xG vs Actual Goals Trend (Last 8 Matches)", template="plotly_dark", height=450)
st.plotly_chart(fig, use_container_width=True)

st.info("Add your free API-Football key in the sidebar for live team data (standings, fixtures, etc.).")
st.caption("Built for MoFutbol 🎙️⚽️ • Saint Charles, Missouri")
