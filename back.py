from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import database
class Item(BaseModel):
    name:str
    roll:int
    clas:str
    rank:str

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "hello world"}
@app.get("/{name}")
async def check(name:str):
    
    return database.search(name)
   
@app.post("/details")
async def add_details(detail:Item):
    database.add(detail)
    return{"added":"successfull"}


