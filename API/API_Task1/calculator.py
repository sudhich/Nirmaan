
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, StrictFloat, StrictInt
from typing import Literal, Union

app = FastAPI(title="Simple Calculator API")

# Pydantic model
class Calculator(BaseModel):
    a: Union[StrictInt, StrictFloat]
    b: Union[StrictInt, StrictFloat]
    operation: Literal[
        "add",
        "subtract",
        "multiply",
        "divide"
    ]

# Calculator function
def calculate(a, b, operation):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        return a / b


# POST API endpoint
@app.post("/calculator")
def calculator_api(data: Calculator):

    result = calculate(
        data.a,
        data.b,
        data.operation
    )

    return {
        "a": data.a,
        "b": data.b,
        "operation": data.operation,
        "result": result,
        "message": "Calculation successful"
    }

# {
#     "a": 20,
#     "b": 10,
#     "operation": "multiply"
# }
#curl -X POST "http://127.0.0.1:8000/calculator" -H "Content-Type: application/json" -d "{\"a\":6,\"b\":4,\"operation\":\"multiply\"}"
