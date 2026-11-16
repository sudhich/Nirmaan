
from fastapi import FastAPI
from pydantic import BaseModel, StrictInt

app = FastAPI(title="Multiplication API")

# Pydantic model for input validation
class Multiply(BaseModel):
    a: StrictInt
    b: StrictInt

# Multiplication function
def multiply(a: int, b: int):
    return a * b

# POST endpoint
@app.post("/multiply")
def multiply_api(data: Multiply):

    result = multiply(data.a, data.b)

    return {
        "a": data.a,
        "b": data.b,
        "result": result,
        "message": "Multiplication successful"
    }
