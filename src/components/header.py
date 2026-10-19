import streamlit as st

def header_home():
  logo_url="https://png.pngtree.com/png-vector/20230808/ourmid/pngtree-gold-graduation-cap-vector-png-image_6884305.png"
  st.markdown(f"""
    <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;margin-bottom:30px;margin-top:30px;">
      <img src={logo_url} height="100px" />
      <h1 style="text-align: center;color:#E0E3FF">SNAP<br/> CLASS</h1>
    </div>
  """,unsafe_allow_html=True)
def header_dashboard():
  logo_url="https://png.pngtree.com/png-vector/20230808/ourmid/pngtree-gold-graduation-cap-vector-png-image_6884305.png"
  st.markdown(f"""
    <div style="display:flex;justify-content:center;align-items:center;margin-bottom:30px;">
      <img src={logo_url} height="85px" />
      <h2 style="text-align: left;color:#5865F2">SNAP<br/> CLASS</h2>
    </div>
  """,unsafe_allow_html=True)
