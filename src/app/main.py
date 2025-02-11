from fastapi import FastAPI
from pydantic import BaseModel
from service import *

app = FastAPI()

class Query(BaseModel):
    question: str
    

@app.post("/get_answer")
def get_answer(query: Query):
    answer = generate_answer(query.question)
    return {"question": query.question, "answer": answer} 




