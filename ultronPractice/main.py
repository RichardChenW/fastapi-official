from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#! 定义 schema


class Data(BaseModel):
    score: Optional[str] = None
    version: Optional[str] = None


class Model(BaseModel):
    code: int
    message: str
    data: Optional[Data] = None


@app.get("/")
def demo(data: Optional[None] = None, response_model=Model):
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
