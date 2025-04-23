import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Daily Motivation", layout="centered")

# Read Excel file (quotes.xlsx should be bundled inside Docker)
@st.cache_data
def load_quotes():
    df = pd.read_excel("quotes.xlsx")
    return df

df = load_quotes()

st.title("🌟 Daily Dose of Motivation")
st.markdown("### Select a number between **0 and 20** to receive your quote!")

number = st.slider("Choose your number:", 0, 20)

if st.button("Get Motivated! 🚀"):
    quote = df.loc[df['ID'] == number, 'Quote'].values[0]
    st.success(f"💬 *{quote}*")
else:
    st.info("Select a number and click the button!")

st.markdown("---")
st.caption("🔒 Quotes are stored securely and cannot be accessed externally.")
