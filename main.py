import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.dates as mdates    


st.title('Visualization homework')
yearslider = st.sidebar.slider('년도',1981,2100)
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


col1, col2 = st.columns([3,2])
with col1:
    df2 = pd.DataFrame({'lat': [42.187,34.355], 'lon' : [123.71945,130.502]})
    st.map(df2)
with col2:
    image = Image.open(cultiva_selectbox + '.jpg')
    image2 = Image.open(cultiva_selectbox + '2.jpg')
    st.image(image)
    st.image(image2)

st3 = pd.read_csv('st3.csv')
df_13 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'_new2.csv').values[0])
df_14= df_13[df_13['Year']==yearslider]
max2012 = df_14['tmax'].mean()
min2012 = df_14['tmin'].mean()
fruit2 = pd.read_csv('fruit2.csv', encoding = 'cp949')
fruit2_1 = fruit2[fruit2['작물명']== cultiva_selectbox]['연평균 최고기온'].values[0]
fruit2_2 = fruit2[fruit2['작물명']== cultiva_selectbox]['연평균 최저기온'].values[0]

if (max2012 >= fruit2_1) & (min2012 <= fruit2_2):
    first_score = 100
    nansu1 = np.exp(abs(max2012 - fruit2_1)/10) 
    nansu2 = np.exp(abs(min2012 - fruit2_2)/10)
    nansu = nansu1 + nansu2
    total_score = first_score - nansu
elif (max2012 >= fruit2_1) & (min2012 >= fruit2_1):
    first_score = 0
    total_score = first_score
elif (max2012<=fruit2_1) & (max2012>=fruit2_2) & (min2012<= fruit2_2):
    first_score = (max2012-fruit2_2)/(fruit2_1 - fruit2_2)*100
    nansu1 = np.exp(abs(min2012 - fruit2_2)/10)
    total_score = first_score - nansu1
else:
    first_score = (fruit2_1-min2012)/(fruit2_1 - fruit2_2)*100
    nansu1 = np.exp(abs(max2012 - fruit2_1)/10) 
    total_score = first_score - nansu1

data_frame2 = {'total_score' : round(total_score,2),'nonscore' : 100-round(total_score,2)}
data_frame = {'score' : 70,'nonscore' : 30}

col1_1, col1_2 = st.columns([2,1])
with col1_1:
    fig = plt.figure(1)
    ax = fig.add_subplot()
    colors = ['lightgreen','white']
    ax.pie([data_frame['score'],data_frame['nonscore']],colors = colors, explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig.gca().add_artist(centre_circle)
    ax.text(-0.,0,data_frame['score'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('Total', size = 20)
    st.pyplot(fig)
with col1_2:
    fig2 = plt.figure(2)
    ax2 = fig2.add_subplot()
    colors = ['gray','white']
    ax2.pie([data_frame2['total_score'],data_frame2['nonscore']],colors = ['gray','white'], explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig2.gca().add_artist(centre_circle)
    ax2.text(-0.,0,data_frame2['total_score'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('Year', size = 20)
    st.pyplot(fig2)

    fig3 = plt.figure(3)
    ax3 = fig3.add_subplot()
    colors = ['lightblue','white']
    ax3.pie([data_frame['score'],data_frame['nonscore']],colors = colors, explode = (0.05,0.05))
    centre_circle = plt.Circle((0, 0), 0.90, fc='white')
    fig3.gca().add_artist(centre_circle)
    ax3.text(-0.,0,data_frame['score'], size = 20, horizontalalignment='center', verticalalignment='center')
    plt.title('Growth', size = 20)
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
plt.fill_between(x = df2.index, y1= df2['연평균 최고기온'],y2 =df2['tmin'], where = df2['tmin'] > df2['연평균 최고기온'],interpolate= True,  facecolor = 'white', alpha = 1)
plt.fill_between(x = df2.index, y1= df2['연평균 최저기온'],y2 =df2['tmax'], where = df2['tmax'] < df2['연평균 최저기온'],interpolate= True,  facecolor = 'white', alpha = 1)
st.pyplot(fig)

st.subheader(cultiva_selectbox + '의 적정 연간평균 기온과 ' + location_selectbox + '의 특정 연도 기온 비교')
st3 = pd.read_csv('st3.csv')
df = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'_new2.csv').values[0])
df2_1 = df[df['Year']==yearslider]
df2_1 = df2_1.reset_index()
fruit2 = pd.read_csv('fruit2.csv', encoding = 'cp949')
fruit2_1 = fruit2[fruit2['작물명']== cultiva_selectbox]['연평균 최저기온']
fruit2_2 = fruit2[fruit2['작물명']== cultiva_selectbox]['연평균 최고기온']
tavgmin = []
tavgmax = []
for i in range(len(df2_1)):
    tavgmin.append(fruit2_1.values[0])
    tavgmax.append(fruit2_2.values[0])
df2_2 = pd.concat([df2_1,pd.Series(tavgmin).rename('연평균 최저기온'),pd.Series(tavgmax).rename('연평균 최고기온')],axis = 1)
dfodf = []
for i in range(len(df2_2)):    
    dfodf.append(str(df2_2['Mon'][i]) + '/'+str(df2_2['Day'][i]))
df2_2['date'] = dfodf
fig = plt.figure(figsize=(11,4))
plt.plot(df2_2['tmax'], color = 'red')
plt.plot(df2_2['tmin'], color = 'blue')
plt.plot(df2_2['연평균 최저기온'], color = 'lightgray')
plt.plot(df2_2['연평균 최고기온'], color = 'lightgray')
plt.xticks(np.arange(0,365,15), labels = ['Jan','','Feb','','Mar','','Apr','','May','','Jun','','Jul','','Aug','','Sep','','Oct','','Nov','','Dec','',''])
plt.fill_between(x = df2_2.index, y1= df2_2['연평균 최저기온'],y2 =df2_2['tmin'], where = df2_2['tmin'] < df2_2['연평균 최저기온'],interpolate= True,  facecolor = 'blue', alpha = 0.5)
plt.fill_between(x = df2_2.index, y1= df2_2['연평균 최고기온'],y2 =df2_2['tmax'], where = df2_2['tmax'] > df2_2['연평균 최고기온'],interpolate= True,  facecolor = 'red', alpha = 0.5)
plt.fill_between(x = df2_2.index, y1= df2_2['연평균 최고기온'],y2 =df2_2['tmin'], where = df2_2['tmin'] > df2_2['연평균 최고기온'],interpolate= True,  facecolor = 'white', alpha = 1)
plt.fill_between(x = df2_2.index, y1= df2_2['연평균 최저기온'],y2 =df2_2['tmax'], where = df2_2['tmax'] < df2_2['연평균 최저기온'],interpolate= True,  facecolor = 'white', alpha = 1)
st.pyplot(fig)


################################################################
st.subheader('')
st.subheader(cultiva_selectbox + ' 생육시기에서 적정 생육 기온과 ' + location_selectbox + '의 기온 비교')
st3 = pd.read_csv('st3.csv')
fruit2 = pd.read_csv('fruit2.csv', encoding = 'cp949')
fruit5_1 = fruit2[fruit2['작물명']== cultiva_selectbox]['생육 최저기온']
fruit5_2 = fruit2[fruit2['작물명']== cultiva_selectbox]['생육 최고기온']
fruit5_3 = fruit2[fruit2['작물명']== cultiva_selectbox]['생육 시작']
fruit5_4 = fruit2[fruit2['작물명']== cultiva_selectbox]['생육 끝']
df_13 = pd.read_csv((st3[st3['kEname']==location_selectbox]['number']+'_new2.csv').values[0])
df_130 = df_13[df_13['Year']==yearslider]
if (fruit5_4.values[0]-fruit5_3.values[0]) == 2:
    df_131 = df_130[df_130['Mon']==fruit5_3.values[0]]
    df_132 = df_130[df_130['Mon']==fruit5_3.values[0]+1]
    df_231 = df_130[df_130['Mon']==fruit5_4.values[0]]
    df_133 = pd.concat([df_131,df_132,df_231])  
elif (fruit5_4.values[0]-fruit5_3.values[0]) == 4:
    df_131 = df_130[df_130['Mon']==fruit5_3.values[0]]
    df_132 = df_130[df_130['Mon']==fruit5_3.values[0]+1]
    df_1321 = df_130[df_130['Mon']==fruit5_3.values[0]+2]
    df_1322 = df_130[df_130['Mon']==fruit5_3.values[0]+3]
    df_231 = df_130[df_130['Mon']==fruit5_4.values[0]]
    df_133 = pd.concat([df_131,df_132,df_1321, df_1322, df_231])
else :
    df_131 = df_130[df_130['Mon']==fruit5_3.values[0]]
    df_132 = df_130[df_130['Mon']==fruit5_3.values[0]+1]
    df_1321 = df_130[df_130['Mon']==fruit5_3.values[0]+2]
    df_1322 = df_130[df_130['Mon']==fruit5_3.values[0]+3]
    df_1323 = df_130[df_130['Mon']==fruit5_3.values[0]+4]
    df_1324 = df_130[df_130['Mon']==fruit5_3.values[0]+5]
    df_231 = df_130[df_130['Mon']==fruit5_4.values[0]]
    df_133 = pd.concat([df_131,df_132,df_1321, df_1322,df_1323, df_1324, df_231])
df_133 = df_133.reset_index()
tavgmin = []
tavgmax = []
for i in range(len(df_133)):
    tavgmin.append(fruit5_1.values[0])
    tavgmax.append(fruit5_2.values[0])
df_134 = pd.concat([df_133,pd.Series(tavgmin).rename('생육 최저기온'),pd.Series(tavgmax).rename('생육 최고기온')],axis = 1)
fig = plt.figure(figsize=(11,4))
plt.plot(df_134['tmax'], color = 'red')
plt.plot(df_134['tmin'], color = 'blue')
plt.plot(df_134['생육 최저기온'], color = 'lightgray')
plt.plot(df_134['생육 최고기온'], color = 'lightgray')
if fruit5_4.values[0]-fruit5_3.values[0] == 2:
    plt.xticks(np.arange(0,((fruit5_4.values[0]-fruit5_3.values[0])+1)*30,15), labels = ['Mar','','Jun','','Jul',''])

elif fruit5_4.values[0]-fruit5_3.values[0] == 4:
    plt.xticks(np.arange(0,((fruit5_4.values[0]-fruit5_3.values[0])+1)*30,15), labels = ['Mar','','Jun','','Jul','','Aug','','Sep',''])
else:
    plt.xticks(np.arange(0,((fruit5_4.values[0]-fruit5_3.values[0])+1)*30,15), labels = ['Apr','','Mar','','Jun','','Jul','','Aug','','Sep','','Oct',''])
plt.fill_between(x = df_134.index, y1= df_134['생육 최저기온'],y2 =df_134['tmin'], where = df_134['tmin'] < df_134['생육 최저기온'],interpolate= True,  facecolor = 'blue', alpha = 0.5)
plt.fill_between(x = df_134.index, y1= df_134['생육 최고기온'],y2 =df_134['tmax'], where = df_134['tmax'] > df_134['생육 최고기온'],interpolate= True,  facecolor = 'red', alpha = 0.5)
plt.fill_between(x = df_134.index, y1= df_134['생육 최고기온'],y2 =df_134['tmin'], where = df_134['tmin'] > df_134['생육 최고기온'],interpolate= True,  facecolor = 'white', alpha = 1)
plt.fill_between(x = df_134.index, y1= df_134['생육 최저기온'],y2 =df_134['tmax'], where = df_134['tmax'] < df_134['생육 최저기온'],interpolate= True,  facecolor = 'white', alpha = 1)
st.pyplot(fig)

###########################################################################














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
