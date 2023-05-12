from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class InUser(BaseModel):
    name: str
    age: int
    sex: str = None


class OutUser(BaseModel):
    name: str
    age: int


@app.get("/user", response_model=OutUser)
def demo(user: InUser):
    return user


if __name__ == "__main__":
    uvicorn.run("13_响应模型:app", host="127.0.0.2", port=8080, reload=True)
