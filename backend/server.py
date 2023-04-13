import logging
import os
import json

from fastapi import FastAPI, File
import uvicorn

from config import IMG_RECORD_FILE, STATIC_DIR, IMG_RESULT_FILE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = FastAPI()
count = 1


@app.post("/upload")
def upload(file_content: bytes = File()):
    global count
    img_path = os.path.join(STATIC_DIR, f"{count}.jpg")
    with open(img_path, "wb") as f:
        f.write(file_content)
    with open(IMG_RECORD_FILE, "a") as f:
        f.write(img_path)
    return {"code": 200}


@app.post("/img")
def img():
    data = []
    with open(IMG_RESULT_FILE, "r") as f:
        for line in f.readlines():
            data.append(json.loads(line))
    return {"code": 200, "data": data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
