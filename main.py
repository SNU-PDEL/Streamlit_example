import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Visualization homework')
location_selectbox = st.sidebar.selectbox('시군구',('A','B','C'))
cultiva_selectbox = st.sidebar.selectbox('작물',('사과','포도','가지','멜론','방울토마토','배추','브로콜리','상추','양배추','오이','참외','토마토','파프리카','호박','고구마','콩'))

if st.sidebar.button('Custom'):
    col1_1, col1_2 = st.sidebar.columns(2)
    with col1_1:
        st.selectbox('육묘 시작 월',('1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'))
st.sidebar.slider('육묘 적정 기온', 10, 40)
    with col1_2:
        st.selectbox('육묘 끝 월',('1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'))


st.slider('Select a Year', 1980, 2020)
col1, col2 = st.columns(2)
with col1:
    df2 = pd.DataFrame({'lat': [42.187,34.355], 'lon' : [123.71945,130.502]})
    st.map(df2)
