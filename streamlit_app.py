import streamlit as st


t = st.text_area("Enter multiline text")

if t is not None:
    textsplit = t.splitlines()

    for x in textsplit:
        st.write(x)
