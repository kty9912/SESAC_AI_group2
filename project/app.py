import streamlit as st
import requests

fastapi_url = "http://127.0.0.1:8000/"

response = requests.get(fastapi_url)

# 타이틀
st.image('templates/로고2.png')

# 주의사항
st.info('데이터 환경에 따라 쿼리 생성 후 데이터 추출 과정에서 오류가 발생할 수 있습니다.')

# 텍스트 필드에 여러 줄 입력받기
st.subheader('질문창')

message = st.text_area('SQL로 뽑고 싶은 정보를 자세히 작성해주세요.', height = 3)
submit_button = st.button('SUBMIT')

if submit_button:
    
    try:
        data = {"question": message}
        response = requests.post(fastapi_url + "question/", json=data)

        if response.status_code == 200:
            result = response.json()

            # 쿼리문
            st.subheader('쿼리문')
            st.info('이 쿼리는 ~ 계산합니다. 이를 통해 ~ 파악할 수 있습니다. 이 정보는 ~에 활용할 수 있습니다.')
            st.text_area("Query:", result['query'])

            # 결과
            st.subheader('결과 데이터')
            st.text_area("Result Data:", result['result_data'])

            st.success("Item created")
        else:
            st.error(f"Failed to create item. Status code: {response.status_code}")

    except Exception as e:
        st.error(f"Error: {e}")


    
