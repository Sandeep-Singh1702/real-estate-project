import streamlit as st

st.set_page_config(
    page_title="My First App",
    page_icon="❤️"
)

st.title("My First App")

st.write("Hello, this is my web app!")
st.sidebar.success("Select a Demo above.")