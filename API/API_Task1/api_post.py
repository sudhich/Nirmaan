# from fastapi import FastAPI

# app = FastAPI()

# @app.post("/mul")
# def mul(a:int,b:int):
#     return a*b
# #http://127.0.0.1:8000/mul?a=3&b=5 method is not allowed because data is sent through URL.


#Not working just because of pydantic 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Multi(BaseModel):
    a:int
    b:int


def mul(a:int,b:int):
    return a*b

@app.post("/mul")
def mu_n(model:Multi):
    return mul(model.a,model.b)

#Using curl
#curl -X POST "http://127.0.0.1:8000/mul" -H "Content-Type:application/json" -d "{\"a\":6,\"b\":4}"