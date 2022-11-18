import streamlit as st
st.text('hello Streamlit!')
col1, col2 = st.columns([1,4])

with col1:
    html = """
    <div style='
        background-color:red;
        color:white;
    '>
        안녕하세요
    </div>
    """

with col2:
    st.markdown(html, unsafe_allow_html = True)

    view = [100,150,30]
    st.write('# Youtube view')
    st.write('## raw')
    view
    st.write('## bar chart')
    st.bar_chart(view)






