import streamlit as st
import pandas as pd
import numpy as np

st.title('Visualization Homework')
selected_item = st.radio('Radio Part', ('A','B','C'))
if selected_item == 'A':
    st.write('A!!')
elif selected_item == 'B':
    st.write('B!!')
elif selected_item == 'C':
    st.write('C!')