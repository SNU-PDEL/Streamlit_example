import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.graph_objects as go
import plotly.express as px


st.title('Visualization homework')
st.sidebar.slider('년도',1980,2020)
with st.form(key='Form2'):
    with st.sidebar:
        location_selectbox = st.selectbox('시군구',('A','B','C'))
        cultiva_selectbox = st.selectbox('작물',('사과','포도','가지','멜론','방울토마토','배추','브로콜리','상추','양배추','오이','참외','토마토','파프리카','호박','고구마','콩'))
        submitted2 = st.form_submit_button(label = 'submit')

if st.sidebar.button('Custom'):
    with st.form(key = 'Form1'):
        with st.sidebar:  
            st.slider('육묘 기간',1,12, (4,9))
            st.slider('육묘 적정 기온', 10,40,(20,30))
            st.slider('생육 기간', 1,12, (4,9))
            st.slider('생육 적정 기온', 10,40,(20,30))
            submitted1 = st.form_submit_button(label = 'submit')

col1, col2 = st.columns(2)
with col1:
    df2 = pd.DataFrame({'lat': [42.187,34.355], 'lon' : [123.71945,130.502]})
    st.map(df2)

data_frame = {'score' : 70,
              'nonscore' : 30}
fig = px.pie(
    hole = 0.9,
    labels = data_frame.values(),
    values= data_frame.values(),
    names = data_frame.keys())
st.header('Donut chart')
st.plotly_chart(fig)
