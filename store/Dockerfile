# Use a specific version of python slim image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the versions.txt file into the working directory
COPY versions.txt /app/

# Install any needed packages specified in versions.txt
RUN pip install --no-cache-dir -r versions.txt

# Copy the rest of your application into the working directory
COPY . /app

# Run the Uvicorn server on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


