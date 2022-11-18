import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 타이틀
st.title('Title')
# 헤더
st.header('Header')
# 서브헤더
st.subheader('subheader')

# 텍스트 작성
st.write('Write Something')

# 버튼 만들기
if st.button('click button'):
    st.write('Data Loading..')
# 체크 박스 만들기
checkbox_btn = st.checkbox('Checkbox Button')
if checkbox_btn:
    st.write('Great!')
# 라디오 버튼 만들기
st.title('Visualization Homework')
selected_item = st.radio('Radio Part', ('A','B','C'))
if selected_item == 'A':
    st.write('A!!')
elif selected_item == 'B':
    st.write('B!!')
elif selected_item == 'C':
    st.write('C!')

# 선택 박스 만들기
option = st.selectbox('Please select in selectbox!',
                        ('kyle', 'seongyun', 'zzsza'))
st.write('You selected :', option)

# 다중 선택 박스 만들기
multi_select = st.multiselect('Please select something in multi selectbox!',
                                ['A','B','C','D'])
st.write('You selected:', multi_select)

# 슬라이더 만들기
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 텍스트 데이터 입력창
st.text_input('Movie title', '')
# 암호 데이터 입력창
st.text_input('Password', type = 'password')
# 숫자 데이터 입력창 
st.number_input('Insert a Number')
# 텍스트 여러줄 입력창
st.text_area('multi text','')
# 날짜 입력창
st.date_input('Date')
# 시간 입력창
st.time_input('Time')

# 데이터 출력
st.write('st.dataframe api')
df = pd.DataFrame(np.random.randn(5,2), columns = ('col %d' %i for i in range(2)))
st.dataframe(df. style.highlight_max(axis = 0))

st.write('st.table api')
st.table(df)

# line chart
st.line_chart(df)
# area chart
st.area_chart(df)
# bar chart
st.bar_chart(df)
# altair_chart
st.altair_chart(df)
# vega lite chart
st.vega_lite_chart(df)
# plotly chart
st.plotly_chart(df)
# bokeh chart
st.bokeh_chart(df)
# pydeck chart
st.pydeck_chart(df)
# graphviz chart
st.graphviz_chart(df)
# map
st.map(df)