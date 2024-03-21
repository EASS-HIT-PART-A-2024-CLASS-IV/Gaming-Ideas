FROM python:3.9-slim

WORKDIR /my_UI

COPY . /my_UI

RUN pip install --no-cache-dir streamlit pandas

EXPOSE 8501

CMD ["streamlit", "run", "ST.py"]
