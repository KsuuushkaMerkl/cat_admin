FROM python:3.10

WORKDIR /cat_admin_app

COPY . .

RUN pip install --upgrade pip

RUN mkdir -p static

RUN pip install -r requirements.txt

CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload