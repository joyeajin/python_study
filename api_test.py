from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

class Item(BaseModel):
    name: str
    number: int
    
@api.post('/')
async def first_post(item: Item):
    return item

@api.get('/')
async def first():
    hi = '안녕하세요'
    return hi

@api.get('/random_number')
def random_no():
    import random
    val_random_number = random.randint(1, 10)

    return val_random_number

@api.get('/hello')
def hello(name=None, msg=None):
    if name is None or msg is None:
        result_str = 'Hello. No name'
    else:
        result_str = 'Hello. ' + name + msg
    
    return result_str

