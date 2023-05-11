'''
Author: Richard Chen
Date: 2023-05-10 16:33:41
LastEditors: Richard Chen
LastEditTime: 2023-05-10 18:43:32
FilePath: \fastApi-official\10_上传文件.py
Description: 

Copyright (c) 2023 by Richard Chen, All Rights Reserved.
'''

from fastapi import FastAPI, UploadFile, File
import pandas as pd
import uvicorn
import io

app = FastAPI()


@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_excel(contents)
    return df.to_dict()


if __name__ == "__main__":
    uvicorn.run("10_上传文件:app", host="127.0.0.2", port=8080, reload=True)
