import streamlit as st
import pandas as pd
import numpy as np

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