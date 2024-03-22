FROM python:3.9-slim

WORKDIR /db

COPY . /db
COPY versions.txt .

RUN pip install -r versions.txt

CMD ["python", "DB.py"]





