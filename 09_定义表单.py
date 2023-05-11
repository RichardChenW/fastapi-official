'''
Author: Richard Chen
Date: 2023-05-10 16:06:17
LastEditors: Richard Chen
LastEditTime: 2023-05-10 16:35:36
FilePath: \fastApi-official\09_定义表单.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved. 
'''


from fastapi import FastAPI, Form, Header
import uvicorn
from uuid import UUID, uuid4

app = FastAPI()


@app.post("/verify")
def demo(
    username: str = Form(default=None),
    password: str = Form(default=None),
    content_type: str = Header(),
    user_agent: str = Header()
):
    return {
        "account": {
            "username": username,
            "password": password
        },
        "Content-Type": content_type,
        "user_agent": user_agent,
        "UUID": UUID(int=uuid4().int, version=4)
    }


if __name__ == "__main__":
    uvicorn.run("09_定义表单:app", host="127.0.0.1", port=8080, reload=True)
