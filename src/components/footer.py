import streamlit as st

def footer_home():
  logo_url="https://lens.usercontent.google.com/banana?agsi=CmdnbG9iYWw6OjAwMDA1NWNmZWM3MDAyNmQ6MDAwMDAwZWI6MTo4MmY3ZTAxZjEwMjg5ZjQ4OjAwMDA1NWNmZWM3MDAyNmQ6MDAwMDAyZjM0OTcwMzM2ODowMDA2NWQ4MGEwZjhhYzJmEAIYASIKaW1hZ2UvanBlZw=="
  st.markdown(f"""
    <div style="display:flex;gap:6px;justify-content:center;align-items:center;margin-top:2rem;">
      <p style="font-weight:bold;color:white">Created with 🩷 by </p>
      <img src={logo_url} style="max-height: 25px;" />
    </div>
  """,unsafe_allow_html=True)

def footer_dashboard():
  logo_url="https://lens.usercontent.google.com/banana?agsi=CmdnbG9iYWw6OjAwMDA1NWNmZWM3MDAyNmQ6MDAwMDAwZWI6MTo4MmY3ZTAxZjEwMjg5ZjQ4OjAwMDA1NWNmZWM3MDAyNmQ6MDAwMDAyZjM0OTcwMzM2ODowMDA2NWQ4MGEwZjhhYzJmEAIYASIKaW1hZ2UvanBlZw=="
  st.markdown(f"""
    <div style="display:flex;gap:6px;justify-content:center;align-items:center;margin-top:2rem;">
      <p style="font-weight:bold;color:black">Created with 🩷 by </p>
      <img src={logo_url} style="max-height: 25px;" />
    </div>
  """,unsafe_allow_html=True)
