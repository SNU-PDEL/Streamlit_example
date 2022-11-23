import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.title('Visualization homework')
st.sidebar.slider('년도',1980,2100)
with st.form(key='Form2'):
    with st.sidebar:
        location_selectbox = st.selectbox('시군구',('강릉','강화','거제','거창','고흥','광주','구미','군산','금산','남원','남해','대관령','대구','대전','목포','문경','밀양','보령','보은','부산','부안','부여','산청','서귀포','서산','서울','성산','속초','수원','양평','여수','영덕','영주','영천','완도','울산','울진','원주','의성','이천','인제','인천','임실','장흥','전주','정읍','제주','제천','진주','천안','청주','추풍령','춘천','충주','통영','포항','합천','해남','홍천'))
        cultiva_selectbox = st.selectbox('작물',('단감','당귀','배','복숭아','사과','인삼','천궁','포도','기타'))
        submitted2 = st.form_submit_button(label = 'submit')

if st.sidebar.button('Custom'):
    with st.form(key = 'Form1'):
        with st.sidebar:  
            st.slider('연 평균 기온', 10,40,(20,30))
            st.slider('생육 기간', 1,12, (4,9))
            st.slider('생육 적정 기온', 10,40,(20,30))
            submitted1 = st.form_submit_button(label = 'submit')

data_frame = {'score' : 70,'nonscore' : 30}

col1, col2 = st.columns([3,2])
with col1:
    df2 = pd.DataFrame({'lat': [42.187,34.355], 'lon' : [123.71945,130.502]})
    st.map(df2)

col1_1, col1_2 = st.columns([2,1])
with col1_1:
    fig = plt.figure(1)
    ax = fig.add_subplot()
    colors = ['lightgreen','white']
    ax.pie([data_frame['score'],data_frame['nonscore']],colors = colors, explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig.gca().add_artist(centre_circle)
    ax.text(-0.,0,data_frame['score'], size = 20, horizontalalignment='center', verticalalignment='center')
    st.pyplot(fig)
with col1_2:
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot()
    colors = ['gray','white']
    ax2.pie([data_frame['nonscore'],data_frame['score']],colors = ['gray','white'], explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig2.gca().add_artist(centre_circle)
    ax2.text(-0.,0,data_frame['nonscore'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('seedling', size = 20)
    st.pyplot(fig2)

    fig3 = plt.figure(3)
    ax3 = fig3.add_subplot()
    colors = ['lightblue','white']
    ax3.pie([data_frame['score'],data_frame['nonscore']],colors = colors, explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig3.gca().add_artist(centre_circle)
    ax3.text(-0.,0,data_frame['score'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('growth', size = 15)
    st.pyplot(fig3)


#st.subheader(location_selectbox + '의 최고기온, 최저기온')
#st3 = pd.read_csv('st3.csv')
#df = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'_new2.csv').values[0])
#df2 = df.groupby('Year').max()['tmax']
#df3 = df.groupby('Year').min()['tmin']
#df4 = pd.concat([df2,df3], axis = 1)
#fig = plt.figure(figsize=(11,4))
#plt.plot(df4['tmax'], color = 'red')
#plt.plot(df4['tmin'], color = 'blue')
#plt.legend(['tmax','tmin'])
#st.pyplot(fig)

st.subheader(cultiva_selectbox + '의 적정 연간평균 기온과 ' + location_selectbox + '의 연간 기온 비교')
st3 = pd.read_csv('st3.csv')
fruit2 = pd.read_csv('fruit2.csv', encoding = 'cp949')
fruit2_1 = fruit2[fruit2['작물명']== cultiva_selectbox]['연평균 최저기온']
fruit2_2 = fruit2[fruit2['작물명']== cultiva_selectbox]['연평균 최고기온']
df = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'_new2.csv').values[0])
tavgmin = []
tavgmax = []
for i in range(len(df)):
    tavgmin.append(fruit2_1.values[0])
    tavgmax.append(fruit2_2.values[0])
df1_1 = pd.concat([df,pd.Series(tavgmin).rename('연평균 최저기온'),pd.Series(tavgmax).rename('연평균 최고기온')],axis = 1)
df2 = df1_1.groupby('Year').mean()[['tmax','tmin','연평균 최저기온','연평균 최고기온']] 
fig = plt.figure(figsize=(11,4))
plt.plot(df2['tmax'], color = 'red')
plt.plot(df2['tmin'], color = 'blue')
plt.plot(df2['연평균 최저기온'], color = 'lightgray')
plt.plot(df2['연평균 최고기온'], color = 'lightgray')
plt.legend(['tmax','tmin','optimal_tmin','optimal_tmax'], loc = 'upper left')
plt.fill_between(x = df2.index, y1= df2['연평균 최저기온'],y2 =df2['tmin'], where = df2['tmin'] < df2['연평균 최저기온'],interpolate= True,  facecolor = 'blue', alpha = 0.5)
plt.fill_between(x = df2.index, y1= df2['연평균 최고기온'],y2 =df2['tmax'], where = df2['tmax'] > df2['연평균 최고기온'],interpolate= True,  facecolor = 'red', alpha = 0.5)
st.pyplot(fig)

################################################################
st.subheader('')
st.subheader(cultiva_selectbox + ' 생육시기에 대한 ' + location_selectbox + '의 기온 변화 추이')
st3 = pd.read_csv('st3.csv')
fruit2 = pd.read_csv('fruit2.csv', encoding = 'cp949')
fruit2_1 = fruit2[fruit2['작물명']== cultiva_selectbox]['생육 최저기온']
fruit2_2 = fruit2[fruit2['작물명']== cultiva_selectbox]['생육 최고기온']
df_13 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'.csv').values[0])
df_23 = df_13.groupby(['Year','Mon']).max()
df_33 = df_13.groupby(['Year','Mon']).min()

if int(fruit2[fruit2['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit2[fruit2['작물명']== cultiva_selectbox]['생육 시작']) == 2:
    fruit23 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit24 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit25 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit33 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit34 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit35 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)    
    realtmax = []
    for i in range(len(fruit23)):
        realtmax.append(fruit23.iloc[i]['tmax'])
        realtmax.append(fruit24.iloc[i]['tmax'])
        realtmax.append(fruit25.iloc[i]['tmax'])
    realtmin = []    
    for i in range(len(fruit23)):
        realtmin.append(fruit33.iloc[i]['tmin'])
        realtmin.append(fruit34.iloc[i]['tmin'])
        realtmin.append(fruit35.iloc[i]['tmin'])
    dfYear= []
    for i in fruit23.index:
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
    dfMonth = []
    for i in fruit23.index:
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작']))
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+1)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 끝']))
    realfruit = pd.DataFrame({'Year' : dfYear, 'Mon': dfMonth, 'tmax' : realtmax, 'tmin' : realtmin})        

elif int(fruit2[fruit2['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit2[fruit2['작물명']== cultiva_selectbox]['생육 시작']) == 4:
    fruit23 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit24 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit25 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit26 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+3,axis = 0, level = 1)
    fruit27 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit33 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit34 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit35 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit36 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+3,axis = 0, level = 1)
    fruit37 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    
    realtmax = []
    for i in range(len(fruit23)):
        realtmax.append(fruit23.iloc[i]['tmax'])
        realtmax.append(fruit24.iloc[i]['tmax'])
        realtmax.append(fruit25.iloc[i]['tmax'])
        realtmax.append(fruit26.iloc[i]['tmax'])
        realtmax.append(fruit27.iloc[i]['tmax'])
    realtmin = []    
    for i in range(len(fruit23)):
        realtmin.append(fruit33.iloc[i]['tmin'])
        realtmin.append(fruit34.iloc[i]['tmin'])
        realtmin.append(fruit35.iloc[i]['tmin'])
        realtmin.append(fruit36.iloc[i]['tmin'])
        realtmin.append(fruit37.iloc[i]['tmin'])
    dfYear= []
    for i in fruit23.index:
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
    dfMonth = []
    for i in fruit23.index:
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작']))
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+1)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+2)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+3)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 끝']))
    realfruit = pd.DataFrame({'Year' : dfYear, 'Mon': dfMonth, 'tmax' : realtmax, 'tmin' : realtmin})        

elif int(fruit2[fruit2['작물명']== cultiva_selectbox]['생육 끝']) - int(fruit2[fruit2['작물명']== cultiva_selectbox]['생육 시작']) == 5:
    fruit23 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit24 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit25 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit26 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+3,axis = 0, level = 1)
    fruit27 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+4,axis = 0, level = 1)
    fruit28 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit33 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit34 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit35 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit36 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+3,axis = 0, level = 1)
    fruit37 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+4,axis = 0, level = 1)
    fruit38 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    
    realtmax = []
    for i in range(len(fruit23)):
        realtmax.append(fruit23.iloc[i]['tmax'])
        realtmax.append(fruit24.iloc[i]['tmax'])
        realtmax.append(fruit25.iloc[i]['tmax'])
        realtmax.append(fruit26.iloc[i]['tmax'])
        realtmax.append(fruit27.iloc[i]['tmax'])
        realtmax.append(fruit28.iloc[i]['tmax'])
    realtmin = []    
    for i in range(len(fruit23)):
        realtmin.append(fruit33.iloc[i]['tmin'])
        realtmin.append(fruit34.iloc[i]['tmin'])
        realtmin.append(fruit35.iloc[i]['tmin'])
        realtmin.append(fruit36.iloc[i]['tmin'])
        realtmin.append(fruit37.iloc[i]['tmin'])
        realtmin.append(fruit38.iloc[i]['tmin'])
    dfYear= []
    for i in fruit23.index:
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
    dfMonth = []
    for i in fruit23.index:
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작']))
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+1)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+2)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+3)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+4)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 끝']))
    realfruit = pd.DataFrame({'Year' : dfYear, 'Mon': dfMonth, 'tmax' : realtmax, 'tmin' : realtmin})        

else:
    fruit23 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit24 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit25 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit26 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+3,axis = 0, level = 1)
    fruit27 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+4,axis = 0, level = 1)
    fruit28 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+5,axis = 0, level = 1)
    fruit29 = df_23.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    fruit33 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작']),axis = 0, level = 1) 
    fruit34 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+1,axis = 0, level = 1)
    fruit35 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+2,axis = 0, level = 1)
    fruit36 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+3,axis = 0, level = 1)
    fruit37 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+4,axis = 0, level = 1)
    fruit38 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 시작'])+5,axis = 0, level = 1)
    fruit39 = df_33.xs(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 끝']),axis = 0, level = 1)
    
    realtmax = []
    for i in range(len(fruit23)):
        realtmax.append(fruit23.iloc[i]['tmax'])
        realtmax.append(fruit24.iloc[i]['tmax'])
        realtmax.append(fruit25.iloc[i]['tmax'])
        realtmax.append(fruit26.iloc[i]['tmax'])
        realtmax.append(fruit27.iloc[i]['tmax'])
        realtmax.append(fruit28.iloc[i]['tmax'])
        realtmax.append(fruit29.iloc[i]['tmax'])
    realtmin = []    
    for i in range(len(fruit23)):
        realtmin.append(fruit33.iloc[i]['tmin'])
        realtmin.append(fruit34.iloc[i]['tmin'])
        realtmin.append(fruit35.iloc[i]['tmin'])
        realtmin.append(fruit36.iloc[i]['tmin'])
        realtmin.append(fruit37.iloc[i]['tmin'])
        realtmin.append(fruit38.iloc[i]['tmin'])
        realtmin.append(fruit39.iloc[i]['tmin'])
    dfYear= []
    for i in fruit23.index:
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
        dfYear.append(i)
    dfMonth = []
    for i in fruit23.index:
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작']))
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+1)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+2)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+3)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+4)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 시작'])+5)
        dfMonth.append(int(fruit2[fruit2['작물명']=='사과']['생육 끝']))
    realfruit = pd.DataFrame({'Year' : dfYear, 'Mon': dfMonth, 'tmax' : realtmax, 'tmin' : realtmin})        

realomin = []
for i in range(len(realfruit)):
    realomin.append(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 최저기온']))
realomax = []
for i in range(len(realfruit)):
    realomax.append(int(fruit2[fruit2['작물명']==cultiva_selectbox]['생육 최고기온']))
realfruit['optimal tmin'] = realomin
realfruit['optimal tmax'] = realomax

fig = plt.figure(figsize=(11,4))
plt.plot(realfruit['optimal tmin'], color = 'lightgray')
plt.plot(realfruit['optimal tmax'], color = 'lightgray')
plt.plot(realfruit['tmax'], color = 'red')
plt.plot(realfruit['tmin'], color = 'blue')

plt.fill_between(x = realfruit['Year'], y1= realfruit['optimal tmin'],y2 =realfruit['tmin'], where = (realfruit['Year']['tmin'] < realfruit['Year']['optimal tmin']),interpolate= True, facecolor = 'blue', alpha = 0.5)
plt.fill_between(x = realfruit['Year'], y1= realfruit['optimal tmax'],y2 =realfruit['tmax'], where = (realfruit['Year']['tmax'] > realfruit['Year']['optimal tmax']),interpolate= True, facecolor = 'red', alpha = 0.5)

plt.legend(['optimal tmax','optimal tmin','tmax','tmin'])
st.pyplot(fig)



year = [1980,1981,1982,1983,1984,1985,1986]
da58 = {'7/1' : [1, 0, 0, 0, 1, 5, 3],
        '7/2' : [1, 0, 0, 0, 0, 2, 4],
        '7/3' : [0, 0, 3, 0, 5, 2, 0],
        '7/4' : [3, 2, 4, 0, 0, 0, 0],
        '7/5' : [6, 2, 4, 1, 0, 0, 1],
        '7/6' : [2, 0, 3, 0, 0, 0, 0],
       }




st.subheader('')
st.subheader(cultiva_selectbox + '의 육묘 적정 기온구간과 ' + location_selectbox+'의 기온구간의 차이')   
heatmap = pd.read_csv('육묘_' + cultiva_selectbox + '_' + location_selectbox + '.csv')
heatmap['cal_total'] = heatmap['cal_tmax'] + heatmap['cal_tmin']
heat = []
for i in range(len(heatmap)):
    heat.append(str(heatmap['Mon'][i]) +'/'+ str(heatmap['Day'][i]))
heatmap['date'] = heat
heat_pivot = heatmap.pivot(['Year'],['date'],['cal_total'])
fig, ax = plt.subplots(figsize=(24, 20))
im = ax.matshow(heat_pivot, cmap='Reds')
ax.grid(False)
fig.colorbar(im)
st.pyplot(fig)

st.subheader('')
st.subheader(cultiva_selectbox + '의 생육 적정 기온구간과 ' + location_selectbox+'의 기온구간의 차이')   
heatmap2 = pd.read_csv('생육_' + cultiva_selectbox + '_' + location_selectbox + '.csv') 
heatmap2['cal_total'] = heatmap2['cal_tmax'] + heatmap2['cal_tmin']
heat2 = []
for i in range(len(heatmap2)):
    heat2.append(str(heatmap2['Mon'][i]) +'/'+ str(heatmap2['Day'][i]))
heatmap2['date'] = heat2
heat_pivot2 = heatmap2.pivot(['Year'],['date'],['cal_total'])
fig, ax = plt.subplots(figsize=(24, 20))
im = ax.matshow(heat_pivot2, cmap='Blues')
#ax.set_xticks(np.arange(len(da58.keys())), labels=da58.keys(), size = 25)
#ax.set_yticks(np.arange(len(year)), labels=year, size = 25)
ax.grid(False)
fig.colorbar(im)
st.pyplot(fig)
