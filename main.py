import streamlit as st
st.text('hello Streamlit!')

html = """
    <div style='
        background-color:red;
        color:white;
    '>
        안녕하세요
    </div>
"""

st.markdown(html, unsafe_allow_html = True)