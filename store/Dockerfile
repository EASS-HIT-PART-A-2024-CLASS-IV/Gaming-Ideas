FROM python:3.10-slim

WORKDIR /shira

COPY versions.txt .

COPY . /shira

RUN pip install -r versions.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0",  "--port", "8000"]












