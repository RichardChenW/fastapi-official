from fastapi import FastAPI, Header
from typing import Union
import uvicorn

app = FastAPI()

@app.get("/")
def demo(user_agent:str=Header(),host:str=Header(),method:str=Header()):
    return {
        "Header":{
            "User-Agent":user_agent,
            "Host":host,
        }
    }

if __name__ == "__main__":
    uvicorn.run("08_声明header请求头:app", host="127.0.0.1",
                port=8000, reload=True)