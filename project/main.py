from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal
from sqlalchemy.orm import Session
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory = "templates")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# nl2sql 모델을 이용하여 질문에 해당하는 쿼리문 가져오는 함수
def generate_sql_query(question: str):
    
    sql_query = "question 결과값"

    return sql_query


# 쿼리문에 해당하는 데이터표 가져오는 함수
def execute_sql_query(db: Session, sql_query: str):
    try:
        # SQL 쿼리 실행
        result = db.execute(sql_query)

        # 결과를 DataFrame으로 변환
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

        # 행별로 딕셔너리 변환
        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing SQL query: {str(e)}")




############# 백엔드 API #############
# 파이썬 강좌 게시판 전체 게시물 보기
@app.get("/acquery/")
def read_homepage(request: Request):
        
        return templates.TemplateResponse(
            "main.html", {
                "request": request
            }
        )

# 새 게시판 글 저장
@app.post("/acquery/question")
def new_post_post(request: Request, db: Session = Depends(get_db)):
    try:
        data = request.json()
        question = data["question"]

        # nl2sql 모델로 question을 보내서 쿼리문을 받아옴
        sql_query = generate_sql_query(question)
        # 쿼리문을 현재 db에 적용하여 해당 데이터표 가져옴
        data_dict = execute_sql_query(db, sql_query)

        # result값을 적절한 json(딕셔너리) 형식으로 변환하여 보내줌
        result = {
            'query': sql_query,
            'result_data': data_dict
        }

        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")