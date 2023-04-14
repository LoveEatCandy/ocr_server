import uuid
import requests
import base64
import hashlib
import io

import retry

from config import APP_KEY, APP_SECRET

YOUDAO_URL = "https://openapi.youdao.com/ocrtransapi"


def encrypt(signStr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signStr.encode("utf-8"))
    return hash_algorithm.hexdigest()


@retry.retry(Exception, tries=3, delay=1)
def translate(
    file_obj: io.BytesIO,
):
    q = base64.b64encode(file_obj.read()).decode("utf-8")
    salt = str(uuid.uuid1())
    signStr = APP_KEY + q + salt + APP_SECRET
    sign = encrypt(signStr)

    data = {
        "from": "en",
        "to": "zh-CHS",
        "type": "1",
        "q": q,
        "appKey": APP_KEY,
        "render": "1",
        "salt": salt,
        "sign": sign,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    return requests.post(YOUDAO_URL, data=data, headers=headers).json()
