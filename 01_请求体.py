'''
Author: Richard Chen
Date: 2023-05-08 22:02:41
LastEditors: Richard Chen
LastEditTime: 2023-05-10 13:28:00
FilePath: \fastApi-offcial\01_请求体.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''


from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def test(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run("01_请求体:app", host="127.0.0.1", port=8000, reload=True)
