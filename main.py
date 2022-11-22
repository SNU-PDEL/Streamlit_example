import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt




st.title('Visualization homework')
st.sidebar.slider('년도',1980,2020)
with st.form(key='Form2'):
    with st.sidebar:
        location_selectbox = st.selectbox('시군구',('강릉','강화','거제','거창','고창','고흥','광주','구미','군산','금산','남원','남해','대관령','대구','대전','목포','문경','밀양','보령','보은','봉화','부산','부안','부여','산청','서귀포','서산','서울','성산','속초','수원','안동','양평','여수','영덕','영주','영천','완도','울릉도','울산','울진','원주','의성','이천','인제','인천','임실','장흥','전주','정읍','제주','제천','진주','천안','청주','추풍령','춘천','충주','통영','포항','합천','해남','홍천'))
        cultiva_selectbox = st.selectbox('작물',('사과','가지','멜론','배추','브로콜리','상추','양배추','파프리카','호박','고구마'))
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
with col2:
    image = Image.open('20221122_095333.png')
    st.image(image)

data_frame = {'score' : 70,
              'nonscore' : 30}
fig = px.pie(
    hole = 0.9,
    values= data_frame.values(),
    color=data_frame.keys(),
    color_discrete_map={'score' : 'royalblue', 'nonscore' : 'white'})
st.header('Donut chart')
st.plotly_chart(fig)

st.subheader('Average annual temperature for 40 years')
st3 = pd.read_csv('st3.csv')
df = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df2 = df.groupby('Year').mean()[['tmax','tmin']]
st.line_chart(df2)

st.subheader('40년간 육묘적정온도 비교')
df_1 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df_2 = df_1.groupby(['Year','Mon']).mean()
fruit = pd.read_csv('fruit.csv', encoding = 'cp949')
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
fig = plt.figure()
plt.plot(fruit2[['tmax','tmin','optimal tmin','optimal tmax']])
plt.fill_between(x = fruit2.index, y1= fruit2['optimal tmin'],y2 =fruit2['optimal tmax'], color = 'green', alpha = 0.5)
st.pyplot(fig)

####################################################################################

st.subheader('40년간 육묘적정온도 비교(최대값)')
df_11 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df_21 = df_11.groupby(['Year','Mon']).max()
fruit = pd.read_csv('fruit.csv', encoding = 'cp949')
if int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']) == 0:
    fruit3 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1)
    fruit3['Unnamed: 0'] = fruit3.index
    fruit3['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])
    fruit3 = fruit3.sort_values('Unnamed: 0')
    fruit_total = fruit3.set_index(['Unnamed: 0', 'Mon'])
elif int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']) == 1:
    fruit3 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1)
    fruit3['Unnamed: 0'] = fruit3.index
    fruit3['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])
    fruit4 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1)
    fruit4['Unnamed: 0'] = fruit4.index
    fruit4['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝'])
    fruit5 = pd.concat([fruit3,fruit4])
    fruit5 = fruit5.sort_values('Unnamed: 0')
    fruit_total = fruit5.set_index(['Unnamed: 0', 'Mon'])
elif int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['육묘 시작']) == 2:
    fruit3 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1)
    fruit3['Unnamed: 0'] = fruit3.index
    fruit3['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])
    fruit4 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+1,axis = 0, level = 1)
    fruit4['Unnamed: 0'] = fruit4.index
    fruit4['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+1
    fruit5 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1)
    fruit5['Unnamed: 0'] = fruit5.index
    fruit5['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝'])
    fruit6 = pd.concat([fruit3,fruit4,fruit5])
    fruit6 = fruit5.sort_values('Unnamed: 0')
    fruit_total = fruit5.set_index(['Unnamed: 0', 'Mon'])
else:
    fruit3 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작']),axis = 0, level = 1)
    fruit3['Unnamed: 0'] = fruit3.index
    fruit3['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])
    fruit4 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+1,axis = 0, level = 1)
    fruit4['Unnamed: 0'] = fruit4.index
    fruit4['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+1
    fruit5 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+2,axis = 0, level = 1)
    fruit5['Unnamed: 0'] = fruit5.index
    fruit5['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 시작'])+2
    fruit6 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝']),axis = 0, level = 1)
    fruit6['Unnamed: 0'] = fruit6.index
    fruit6['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 끝'])
    fruit7 = pd.concat([fruit3,fruit4,fruit5,fruit6])
    fruit7 = fruit7.sort_values('Unnamed: 0')
    fruit_total = fruit7.set_index(['Unnamed: 0', 'Mon'])

fruit_total['optimal tmin'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 최저기온'])
fruit_total['optimal tmax'] = int(fruit[fruit['작물명']==cultiva_selectbox]['육묘 최고기온'])

new_index = []
for i in range(len(fruit_total.index)):
    new_index.append(str(fruit_total.index[i][0]) +'_' +  str(fruit_total.index[i][1]))
fruit_total['new_index'] = new_index

st.line_chart(fruit_total, x = 'new_index')


################################################################
st.subheader('40년간 생육적정온도 비교')
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

st.line_chart(fruit2[['tmax','tmin','optimal tmin', 'optimal tmax']])

####################################################################################

st.subheader('40년간 생육적정온도 비교(최대값)')
df_14 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df_24 = df_14.groupby(['Year','Mon']).max()
fruit = pd.read_csv('fruit.csv', encoding = 'cp949')
if int(fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']) == 0:
    fruit34 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1)
    fruit34['Unnamed: 0'] = fruit34.index
    fruit34['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])
    fruit34 = fruit34.sort_values('Unnamed: 0')
    fruit_total4 = fruit34.set_index(['Unnamed: 0', 'Mon'])
elif int(fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']) == 1:
    fruit34 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1)
    fruit34['Unnamed: 0'] = fruit34.index
    fruit34['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])
    fruit44 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit44['Unnamed: 0'] = fruit44.index
    fruit44['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝'])
    fruit54 = pd.concat([fruit34,fruit44])
    fruit54 = fruit54.sort_values('Unnamed: 0')
    fruit_total4 = fruit54.set_index(['Unnamed: 0', 'Mon'])
elif int(fruit[fruit['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit[fruit['작물명']== cultiva_selectbox]['생육 시작']) == 2:
    fruit34 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1)
    fruit34['Unnamed: 0'] = fruit34.index
    fruit34['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])
    fruit44 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit44['Unnamed: 0'] = fruit44.index
    fruit44['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+1
    fruit54 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit54['Unnamed: 0'] = fruit54.index
    fruit54['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝'])
    fruit64 = pd.concat([fruit34,fruit44,fruit54])
    fruit64 = fruit54.sort_values('Unnamed: 0')
    fruit_total4 = fruit54.set_index(['Unnamed: 0', 'Mon'])
else:
    fruit34 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1)
    fruit34['Unnamed: 0'] = fruit34.index
    fruit34['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])
    fruit44 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit44['Unnamed: 0'] = fruit44.index
    fruit44['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+1
    fruit54 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit54['Unnamed: 0'] = fruit54.index
    fruit54['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 시작'])+2
    fruit64 = df_21.xs(int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit64['Unnamed: 0'] = fruit64.index
    fruit64['Mon'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 끝'])
    fruit74 = pd.concat([fruit34,fruit44,fruit54,fruit64])
    fruit74 = fruit74.sort_values('Unnamed: 0')
    fruit_total4 = fruit74.set_index(['Unnamed: 0', 'Mon'])

fruit_total4['optimal tmin'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 최저기온'])
fruit_total4['optimal tmax'] = int(fruit[fruit['작물명']==cultiva_selectbox]['생육 최고기온'])

new_index4 = []
for i in range(len(fruit_total4.index)):
    new_index4.append(str(fruit_total4.index[i][0]) +'_' +  str(fruit_total4.index[i][1]))
fruit_total4['new_index'] = new_index4

st.line_chart(fruit_total4, x = 'new_index')

