# Dockerfile

# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /store

# Copy the requirements file into the container
COPY versions.txt .

# Install dependencies
RUN pip install --no-cache-dir -r versions.txt

# Copy the rest of the application code into the container
COPY . /store

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]








