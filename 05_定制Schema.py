'''
Author: Richard Chen
Date: 2023-05-10 14:29:03
LastEditors: Richard Chen
LastEditTime: 2023-05-10 14:35:13
FilePath: \fastApi-offcial\05_定制Schema.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''

from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    uvicorn.run("05_定制Schema:app", host="127.0.0.1",port=8000, reload=True)
