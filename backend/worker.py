import base64
import json
import logging
import os
import time

from config import IMG_RECORD_FILE, IMG_RESULT_FILE, STATIC_DIR
from utils import translate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("worker")


def main():
    with open(IMG_RESULT_FILE, "r") as f:
        lines = f.read()
    records = {}
    for line in lines.split("\n"):
        if line:
            line = json.loads(line)
            records[line["origin"]] = line
    logger.info("init success")
    while True:
        with open(IMG_RECORD_FILE, "r") as f:
            imgs = f.read()
        for img in imgs.split("\n"):
            if img and img not in records:
                logger.info(f"translating {img}")
                with open(img, "rb") as f:
                    trans_record = translate(f)
                origin_img_name = os.path.basename(img).split(".")[0]
                translated_img_path = os.path.join(
                    STATIC_DIR, f"{origin_img_name}-translated.jpg"
                )
                with open(translated_img_path, "wb") as f:
                    f.write(
                        base64.b64decode(trans_record["render_image"].encode("utf-8"))
                    )
                records[img] = dict(
                    origin=img,
                    translated=translated_img_path,
                    text="\n".join([line["text"] for line in trans_record["lines"]]),
                )
                with open(IMG_RESULT_FILE, "a") as f:
                    f.write(json.dumps(records[img]) + "\n")
                logger.info(f"translated {img} > {translated_img_path}")
        time.sleep(1)
        logger.info("sleep 1s")


if __name__ == "__main__":
    main()
