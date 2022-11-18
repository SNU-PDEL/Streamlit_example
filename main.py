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
        location_selectbox = st.selectbox('시군구',('강릉','강화','거제','거창','고창','고흥','광주','구미','군산','금산','남원','남해','대관령','대구','대전','목포','문경','밀양','보령','보은','봉화','부산','부안','부여','산청','서귀포','서산','서울','성산','속초','수원','안동','양평','여수','영덕','영주','영천','완도','울릉도','울산','울진','원주','의성','이천','인제','인천','임실','장흥','전주','정읍','제주','제천','진주','천안','청주','추풍령','춘천','충주','통영','포항','합천','해남','홍천'))
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
    names = data_frame.keys(),
    color=['White','Green'])
st.header('Donut chart')
st.plotly_chart(fig)
st3 = pd.read_csv('st3.csv')
st.write(st3)

#def lchart(X):
df = pd.read_csv((st3[st3['kEname']=='강릉']['number']+'.csv').values[0])
df2 = df.groupby('Year').mean()[['tmax','tmin']]
#lchart(location_selectbox)
st.write(df2)
#    st.line_chart(x = chart_df.index, y = chart_df)

#lchart(location_selectbox)