from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from database import async_session
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.staticfiles import StaticFiles
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost",  # Streamlit 앱이 실행 중인 주소
    "http://localhost:8000",  # Streamlit 앱이 실행 중인 주소와 포트
]

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 실제 사용할 때는 특정 origin을 명시하는 것이 좋습니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory = "templates")
app.mount("/static", StaticFiles(directory="templates"), name="static")

async def get_db() -> AsyncSession:
    try:
        async with async_session() as db:
            yield db
    finally:
        if db:
            await db.close()

# nl2sql 모델을 이용하여 질문에 해당하는 쿼리문 가져오는 함수
def generate_sql_query(question: str):
    
    # question 결과값
    sql_query = "SELECT * FROM f150_open_tbl;"

    return sql_query


# 쿼리문에 해당하는 데이터표 가져오는 함수
async def execute_sql_query(db: AsyncSession, sql_query: str):
    try:
        # SQL 쿼리 실행
        result = await db.execute(sql_query)

        # 결과를 DataFrame으로 변환
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

        # Null 값 처리 후 행별로 딕셔너리 변환
        records = df.where(pd.notna(df), None).to_dict(orient="records")

        return records

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing SQL query: {str(e)}")




############# 백엔드 API #############
# 파이썬 강좌 게시판 전체 게시물 보기
@app.get("/")
def read_homepage():
    return None
    

# 대화문 받아 쿼리문과 데이터 반환
@app.post("/question/")
async def new_question(question: dict, db: AsyncSession = Depends(get_db)):
    try:
        #data = await request.json()
        question = question["question"]

        # nl2sql 모델로 question을 보내서 쿼리문을 받아옴
        sql_query = generate_sql_query(question)
        # 쿼리문을 현재 db에 적용하여 해당 데이터표 가져옴
        data_dict = await execute_sql_query(db, sql_query)
        # result값을 적절한 json(딕셔너리) 형식으로 변환하여 보내줌
        result = {
            'query': sql_query,
            'result_data': data_dict
        }

        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")