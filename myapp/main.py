from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ComputeRequest(BaseModel):
    a: float
    b: float
    method: str = "add"

class ComputeResponse(BaseModel):
    result: float
    detail: str

def heavy_calculation(a: float, b: float, method: str) -> float:
    if method == "add":
        return a + b
    elif method == "mul":
        return a * b
    else:
        raise ValueError(f"未知のmethodです: {method}")

@app.post("/compute", response_model=ComputeResponse)
def compute(req: ComputeRequest):
    try:
        value = heavy_calculation(req.a, req.b, req.method)
        return ComputeResponse(result=value, detail="success")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
