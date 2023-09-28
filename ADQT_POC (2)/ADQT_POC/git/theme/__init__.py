import streamlit as st

# LINK TO THE CSS FILE
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css("theme\color.css")
local_css("theme\style.css")
