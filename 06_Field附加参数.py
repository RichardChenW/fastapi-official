'''
Author: Richard Chen
Date: 2023-05-10 14:29:03
LastEditors: Richard Chen
LastEditTime: 2023-05-10 14:39:42
FilePath: \fastApi-offcial\06_Field附加参数.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''

from typing import Union
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(example="Foo")
    description: Union[str, None] = Field(
        default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: Union[float, None] = Field(default=None, example=3.2)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

if __name__ == "__main__":
    uvicorn.run("06_Field附加参数:app", host="127.0.0.1", port=8000, reload=True)
