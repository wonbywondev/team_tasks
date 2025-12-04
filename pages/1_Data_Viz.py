import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="데이터 시각화", layout="wide")

st.title("📊 팀 대시보드 - 데이터 시각화 페이지")

# 예시 데이터
data = {
    "팀원": ["A", "B", "C", "D"],
    "완료 작업 수": [5, 8, 3, 6]
}
df = pd.DataFrame(data)

st.subheader("팀원별 완료 작업 수 테이블")
st.dataframe(df)

fig = px.bar(df, x="팀원", y="완료 작업 수", title="팀원별 완료 작업 수")
st.plotly_chart(fig, use_container_width=True)
