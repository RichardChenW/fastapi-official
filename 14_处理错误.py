from fastapi import FastAPI,HTTPException
import uvicorn
import http

app = FastAPI()

@app.post("/items/", status_code=http.HTTPStatus.OK) #? 请求成功返回的状态码
def create_item(name: str):
    if name == "foo":
        raise HTTPException(status_code=400, detail="Foo Error")
    return {"name": name}

if __name__ == "__main__":
    uvicorn.run("14_处理错误:app",host="127.0.0.1",port=8080,reload=True)