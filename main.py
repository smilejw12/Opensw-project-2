import streamlit as st
import pandas as pd
import numpy as np


# 데이터 불러오기
df = pd.read_csv('trends-extend.csv')

# 제목
st.title('현재 코로나의 상태는?')

st.header('오늘 코로나19')
st.caption(f'updated: {df.iloc[0, 0]}')
st.subheader('서울')
col1, col2, col3 = st.columns(3)
col1.metric('총 확진자', f'{df.iloc[0, 1]}명', f'{df.iloc[0, 1] - df.iloc[1, 1]}명')
col2.metric('추가 확진자 ', f'{df.iloc[0, 2]}명', f'{df.iloc[0, 2] - df.iloc[1, 2]}명')
col3.metric('사망자', f'{df.iloc[0, 6]}명', f'{df.iloc[0, 6] - df.iloc[1, 6]}명')


st.subheader('전국')
col1, col2, col3 = st.columns(3)
col1.metric('총 확진자', f'{df.iloc[0, 8]}명', f'{df.iloc[0, 8] - df.iloc[1, 8]}명')
col2.metric('추가 확진자 ', f'{df.iloc[0, 9]}명', f'{df.iloc[0, 9] - df.iloc[1, 9]}명')
col3.metric('사망자', f'{df.iloc[0, 12]}명', f'{df.iloc[0, 12] - df.iloc[1, 12]}명')

# 각각의 변수를 만들어 열을 지정함으로써 그래프를 만든다
df_all = df.iloc[:, [0, 1, 4, 8, 11]]
df_all.set_index('서울시 기준일', inplace=True)

df_korea = df.iloc[:, [7, 8, 10, 11, 12]]
df_korea.set_index('전국 기준일', inplace=True)

df_seoul_bar = df.iloc[:, [0, 2, 9]]
df_seoul_bar.set_index('서울시 기준일', inplace=True)

st.header('최근 30일 코로나19 추세')

st.subheader('코로나19 상황')
st.line_chart(df_all[0:30])

st.subheader('추가 확진자')
st.line_chart(df_seoul_bar[0:30])
st.bar_chart(df_seoul_bar[0:30])

st.header('한 달 간격으로 보는 코로나19')

st.subheader('코로나19 상황')
st.line_chart(df_all[::30])

st.subheader('추가 확진자')
st.line_chart(df_seoul_bar[::30])
st.bar_chart(df_seoul_bar[::30])

st.header('데이터')
st.dataframe(df)