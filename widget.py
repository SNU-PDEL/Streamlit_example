import streamlit as st
import pandas as pd
import numpy as np

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

# 텍스트 데이터 입력
st.text_input('Movie title', 'Life of pie')