from fastapi import FastAPI
import uvicorn
import http

app = FastAPI()

@app.post("/items/", status_code=http.HTTPStatus.OK) #? 请求成功返回的状态码
def create_item(name: str):
    return {"name": name}

if __name__ == "__main__":
    uvicorn.run("12_响应状态码:app",host="127.0.0.1",port=8080,reload=True)