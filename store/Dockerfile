FROM python:3.9-slim
WORKDIR /backend
COPY . /backend
RUN pip install --no-cache-dir -r versions.txt
RUN pip install --no-cache-dir sqlalchemy
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


