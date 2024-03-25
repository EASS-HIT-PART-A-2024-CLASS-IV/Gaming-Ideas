FROM python:3.9-slim

WORKDIR /UI

COPY . /UI

COPY . /store
# Copy dependency versions file
COPY versions.txt .

# Install required dependencies
RUN pip install -r versions.txt

CMD ["streamlit", "run", "ST.py"]
