FROM python:3.9-slim

WORKDIR /shiralu

COPY . /app

RUN pip install --no-cache-dir streamlit psycopg2 pandas

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
