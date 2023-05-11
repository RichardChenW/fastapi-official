from fastapi import FastAPI, Cookie
from typing import Union
import uvicorn


app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}


if __name__ == "__main__":
    uvicorn.run("07_声明cookie参数:app", host="127.0.0.1",
                port=8000, reload=True)
