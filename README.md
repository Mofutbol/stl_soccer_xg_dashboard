# ⚽ St. Louis Soccer xG Dashboard

Fully automated Streamlit dashboard for **St. Louis CITY SC**, **StL Ambush**, **France**, and **Senegal** national teams with a built-in lightweight **xG proxy model**.

### Features
- Live standings, fixtures, player stats via API-Football
- Advanced xG / xGA proxy analytics (shots, SOT, possession)
- Interactive Plotly charts (xG vs Actual Goals trends)
- Dedicated xG Analytics Center
- Fully automated – refreshes on every run

### How to Run Locally
```bash
pip install -r requirements.txt
streamlit run stl_soccer_xg_dashboard.py
