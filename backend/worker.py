import base64
import json
import os
import time

from config import IMG_RECORD_FILE, IMG_RESULT_FILE, STATIC_DIR
from utils import translate


def main():
    with open(IMG_RESULT_FILE, "r") as f:
        lines = f.read()
    records = {}
    for line in lines.split("\n"):
        line = json.loads(line)
        records[line["origin"]] = line
    while True:
        with open(IMG_RECORD_FILE, "r") as f:
            imgs = f.read()
        for img in imgs.split("\n"):
            if img not in records:
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
        time.sleep(1)


if __name__ == "__main__":
    main()
