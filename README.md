Upload img, ocr english words and translate to chinese by youdao api.

上传图片并 ocr 翻译成中文，使用有道智云的 API. 

- [注册有道账号](https://ai.youdao.com/)
- [有道 API 文档](https://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E5%9B%BE%E7%89%87%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E5%9B%BE%E7%89%87%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html)

## Installation
```
python3 -m venv backend/.venv
source backend/.venv/bin/activate
pip3 install -r backend/requirements.txt -r backend/requirements-dev.txt
cd frontend
npm install
```
## Run
### Server
```
cd backend
python3 server.py
```
### Worker
```
export APP_KEY=
export APP_SECRET=
python3 worker.py
```
### Frontend
```
cd frontend
npm install
npm run dev
```