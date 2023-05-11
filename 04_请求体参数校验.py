'''
Author: Richard Chen
Date: 2023-05-10 13:58:37
LastEditors: Richard Chen
LastEditTime: 2023-05-10 14:20:57
FilePath: \fastApi-official\04_请求体参数校验.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''

# fastapi 基本框架
from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Union
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field( 
        title="The description of the item", 
        max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

@app.get("/")
def test(item:Item):
    return item


if __name__ == "__main__":
    uvicorn.run("04_请求体参数校验:app", host="127.0.0.1",port=8000, reload=True)