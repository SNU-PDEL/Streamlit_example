import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Visualization homework')
location_selectbox = st.sidebar.selectbox('시군구',('A','B','C'))
cultiva_selectbox = st.sidebar.selectbox('작물',('사과','포도','가지','멜론','방울토마토','배추','브로콜리','상추','양배추','오이','참외','토마토','파프리카','호박','고구마','콩'))
custom_button = st.sidebar.button('Custom')
if st.sidebar.button('Custom'):
    st.sidebar.number_input('')
