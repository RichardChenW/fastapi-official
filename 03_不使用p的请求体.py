'''
Author: Richard Chen
Date: 2023-05-09 15:59:21
LastEditors: Richard Chen
LastEditTime: 2023-05-10 13:27:37
FilePath: \fastApi-offcial\03_不使用p的请求体.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''


from fastapi import FastAPI,Body
from typing import Union
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def test(name: Union[str,None] = Body(),age: Union[int,None] = Body(),job: Union[str,None] = Body(default=None)):
    return {"name":name,"age":age,"job":job}
    

if __name__ == "__main__":
    uvicorn.run("03_不使用p的请求体:app", host="127.0.0.1",port=8000, reload=True)