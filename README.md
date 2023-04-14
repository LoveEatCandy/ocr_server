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