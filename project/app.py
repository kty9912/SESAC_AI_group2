import streamlit as st
import requests
import pandas as pd

fastapi_url = "http://127.0.0.1:8000/"

response = requests.get(fastapi_url)

# 타이틀
st.image('templates/로고2.png', use_column_width=True, width=st.sidebar.width)

# 이미지 파일의 경로
image_path = 'templates/로고2.png'

# CSS 스타일을 사용하여 이미지를 가운데 정렬하면서 원본 비율로 유지하고 컬럼의 너비에 맞게 표시
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{image_path}" style="max-width: 100%; max-height: 100%; object-fit: contain;" alt="Your Image">
    </div>
    """,
    unsafe_allow_html=True
)

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
            result_data = pd.DataFrame(result['result_data'])
            st.table(result_data)

        else:
            st.error(f"Failed to create item. Status code: {response.status_code}")

    except Exception as e:
        st.error(f"Error: {e}")


    
