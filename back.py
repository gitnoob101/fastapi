from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Optional
import database
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"] for stricter
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id:Optional[int]=None
    name:str
    roll:int
    clas:str
    pos:str



@app.get("/")
async def hello():
    return {"message": "hello world"}
@app.get("/{name}")
async def check(name:str):
    
    result=database.search(name)
    if not result:
        return {"result":"not found"}
    else:
        return [dict(row._mapping) for row in result]
   
@app.post("/details")
async def add_details(detail:Item):
    database.add(detail)
    return{"added":"successfull"}


