import base64
import json


def main():
    with open("./test.json", "r") as f:
        resp = json.load(f)
    with open("./test.jpg", "wb") as f:
        f.write(base64.b64decode(resp["render_image"].encode("utf-8")))
    for line in resp["lines"]:
        print(line["text"])


if __name__ == "__main__":
    main()
