import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title('Visualization homework')
st.sidebar.slider('년도',1980,2020)
with st.form(key='Form2'):
    with st.sidebar:
        location_selectbox = st.selectbox('시군구',('강릉','강화','거제','거창','고창','고흥','광주','구미','군산','금산','남원','남해','대관령','대구','대전','목포','문경','밀양','보령','보은','봉화','부산','부안','부여','산청','서귀포','서산','서울','성산','속초','수원','안동','양평','여수','영덕','영주','영천','완도','울릉도','울산','울진','원주','의성','이천','인제','인천','임실','장흥','전주','정읍','제주','제천','진주','천안','청주','추풍령','춘천','충주','통영','포항','합천','해남','홍천'))
        cultiva_selectbox = st.selectbox('작물',('가지','고구마','멜론','배추','브로콜리','사과','상추','양배추','파프리카','호박','기타'))
        submitted2 = st.form_submit_button(label = 'submit')

if st.sidebar.button('Custom'):
    with st.form(key = 'Form1'):
        with st.sidebar:  
            st.slider('육묘 기간',1,12, (4,9))
            st.slider('육묘 적정 기온', 10,40,(20,30))
            st.slider('생육 기간', 1,12, (4,9))
            st.slider('생육 적정 기온', 10,40,(20,30))
            submitted1 = st.form_submit_button(label = 'submit')

data_frame = {'score' : 70,'nonscore' : 30}

col1, col2 = st.columns([3,2])
with col1:
    df2 = pd.DataFrame({'lat': [42.187,34.355], 'lon' : [123.71945,130.502]})
    st.map(df2)
with col2:
    image = Image.open(cultiva_selectbox + '.jpg')
    st.image(image)

col1_1, col1_2 = st.columns([2,1])
with col1_1:
    fig = plt.gcf()
    ax = fig.add_subplot()
    colors = ['lightgreen','white']
    ax.pie([data_frame['score'],data_frame['nonscore']],colors = colors, explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig.gca().add_artist(centre_circle)
    ax.text(-0.,0,data_frame['score'], size = 20, horizontalalignment='center', verticalalignment='center')
    st.pyplot(fig)
with col1_2:
    fig2 = plt.gcf()
    ax2 = fig2.add_subplot()
    colors = ['gray','white']
    ax2.pie([data_frame['nonscore'],data_frame['score']],colors = ['gray','white'], explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig2.gca().add_artist(centre_circle)
    ax2.text(-0.,0,data_frame['nonscore'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('육묘', size = 20)
    st.pyplot(fig2)

    fig3 = plt.gcf()
    ax3 = fig3.add_subplot()
    colors = ['lightblue','white']
    ax3.pie([data_frame['score'],data_frame['nonscore']],colors = colors, explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig3.gca().add_artist(centre_circle)
    ax3.text(-0.,0,data_frame['score'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('생육', size = 15)
    st.pyplot(fig3)

labels = ['Oxygen','Hydrogen']
values = [70, 30]
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.9)])
fig.update_traces(marker = dict(colors = ['lightgreen','white']))
st.plotly_chart(fig)


st.subheader(location_selectbox + '의 평균 연간 기온 추이')
st3 = pd.read_csv('st3.csv')
df = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df2 = df.groupby('Year').mean()[['tmax','tmin']]
fig = plt.figure(figsize=(11,4))
plt.plot(df2['tmax'], color = 'red')
plt.plot(df2['tmin'], color = 'blue')
plt.ylim(bottom = 0)
plt.legend(['tmax','tmin'])
st.pyplot(fig)

st.subheader('')
df_1 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df_2 = df_1.groupby(['Year','Mon']).mean()
fruit = pd.read_csv('fruit.csv', encoding = 'cp949')
st.subheader(cultiva_selectbox + ' 육묘시기에 대한 ' + location_selectbox + '의 기온 변화 추이 (' + str((fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']).values[0])+ '월 ~ ' + str((fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']).values[0]) + '월)')
if int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']) == 0:
    fruit2 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1))/2
elif int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']) == 1:
    fruit2 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1))/2
elif int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']) == 2:
    fruit2 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+1,axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1))/3
else:
    fruit2 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+1,axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+2,axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1))/4

fruit2['optimal tmin'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 최저기온'])
fruit2['optimal tmax'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 최고기온'])
fig = plt.figure(figsize=(11,4))
plt.plot(fruit2['optimal tmin'], color = 'lightgray')
plt.plot(fruit2['optimal tmax'], color = 'lightgray')
plt.plot(fruit2['tmax'], color = 'red')
plt.plot(fruit2['tmin'], color = 'blue')

plt.fill_between(x = fruit2.index, y1= fruit2['optimal tmin'],y2 =fruit2['optimal tmax'], facecolor = 'lightgray', alpha = 0.5)
plt.ylim(bottom = 0)
plt.legend(['optimal tmax','optimal tmin','tmax','tmin'])
st.pyplot(fig)

################################################################
st.subheader('')
st.subheader(cultiva_selectbox + ' 생육시기에 대한 ' + location_selectbox + '의 기온 변화 추이 (' + str((fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']).values[0])+ '월 ~ ' + str((fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']).values[0]) + '월)')
df_13 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df_23 = df_13.groupby(['Year','Mon']).mean()
fruit = pd.read_csv('fruit.csv', encoding = 'cp949')
if int(fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']) == 0:
    fruit23 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1))/2
elif int(fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']) == 1:
    fruit23 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1))/2
elif int(fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']) == 2:
    fruit23 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1))/3
else:
    fruit23 = (df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1) + df_2.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1))/4

fruit23['optimal tmin'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 최저기온'])
fruit23['optimal tmax'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 최고기온'])

fig = plt.figure(figsize=(11,4))
plt.plot(fruit23['optimal tmin'], color = 'lightgray')
plt.plot(fruit23['optimal tmax'], color = 'lightgray')
plt.plot(fruit23['tmax'], color = 'red')
plt.plot(fruit23['tmin'], color = 'blue')

plt.fill_between(x = fruit23.index, y1= fruit23['optimal tmin'],y2 =fruit23['optimal tmax'], facecolor = 'lightgray', alpha = 0.5)
plt.ylim(bottom = 0)
plt.legend(['optimal tmax','optimal tmin','tmax','tmin'])
st.pyplot(fig)