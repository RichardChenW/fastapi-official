'''
Author: Richard Chen
Date: 2023-05-09 15:27:42
LastEditors: Richard Chen
LastEditTime: 2023-05-09 16:41:59
FilePath: \fastApi-official\02_字符串校验.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''

from fastapi import FastAPI,Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
def test(item: str = Query(
        default = None,
        min_length=2,
        max_length=10,
        title="标题",
        description="描述",
      )
    ):
  return item

if __name__ == "__main__":
    uvicorn.run("02_字符串校验:app", host="127.0.0.1", port=8000, reload=True)