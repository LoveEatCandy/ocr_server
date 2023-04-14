import json
import logging
import os

import uvicorn
from fastapi import FastAPI, File
from fastapi.staticfiles import StaticFiles

from config import IMG_RECORD_FILE, IMG_RESULT_FILE, STATIC_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
count = 1


@app.post("/api/upload")
def upload(file_content: bytes = File()):
    global count
    img_path = os.path.join(STATIC_DIR, f"{count}.jpg")
    with open(img_path, "wb") as f:
        f.write(file_content)
    count += 1
    with open(IMG_RECORD_FILE, "a") as f:
        f.write(img_path + "\n")
    return {"code": 200}


@app.post("/api/img")
def img():
    data = []
    with open(IMG_RESULT_FILE, "r") as f:
        for line in f.readlines():
            data.append(json.loads(line))
    return {"code": 200, "data": data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
