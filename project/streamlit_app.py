import streamlit as st
import requests
import pandas as pd

st.title("NL2SQL Query Generator")

# 질문 입력 받기
question = st.text_input("Enter your question:")

if st.button("Generate SQL Query"):
    # FastAPI 서버에 HTTP POST 요청을 보내서 SQL 쿼리 생성 및 결과 가져오기
    response = requests.post("http://127.0.0.1:8000/acquery/question/", json={"question": question})
    
    # 결과를 출력
    if response.status_code == 200:
        result = response.json()
        st.text(f"Generated SQL Query: {result['query']}")
        #st.table(pd.DataFrame(result['result_data']))
    else:
        st.text("Error generating SQL query.")