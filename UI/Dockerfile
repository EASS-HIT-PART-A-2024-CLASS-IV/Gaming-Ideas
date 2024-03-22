FROM python:3.9-slim

WORKDIR /UI

COPY . /UI

store/Dockerfile

# Install required dependencies
RUN pip install -r versions.txt

CMD ["streamlit", "run", "ST.py"]