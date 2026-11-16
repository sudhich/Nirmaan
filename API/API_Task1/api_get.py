#pip install fastapi
#pip install uvicorn
#uvicorn api_get:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def multiply(a:int,b:int ):
    return a*b
#print(multiply(3,4))
#http://127.0.0.1:8000/?a=10&b=20
#http://127.0.0.1:8000/docs
#ngrok
#curl

@app.get("/ad")
def add(a:int,b:int):
    return a+b
#curl "http://127.0.0.1:8000/?a=3&b=4"