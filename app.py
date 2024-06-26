from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import Test
from models import Test2

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()


class Item(BaseModel):
    name : str
    number : int

@app.get("/")
async def first_get():
    example = session.query(Test).all()
    return example

@app.get("/test2")
async def second_get():
    example = session.query(Test2).all()
    return example