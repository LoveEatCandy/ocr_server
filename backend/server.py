import logging

from fastapi import FastAPI, File
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = FastAPI()


@app.post("/upload")
def upload(file_content: bytes = File()):
    return {}


@app.post("/imgs")
def upload():
    return {}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9999)
