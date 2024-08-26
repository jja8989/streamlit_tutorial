import streamlit as st

st.set_page_config(
     page_title="실리콘밸리 AI 인턴십 프로그램",
     page_icon="✈️",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://gsds.snu.ac.kr',
         'About': "# 2024 실리콘밸리 AI 인턴십 프로그램 3기"
     }
 )

st.header("2024 실리콘밸리 AI 인턴십 프로그램 3기")

st.subheader("Streamlit Tutorials")

st.image("./static/img/soongsil.png", use_column_width=True)

