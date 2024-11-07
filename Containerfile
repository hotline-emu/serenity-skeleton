# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the Python application and test code into the container
COPY requirements.txt .
COPY features/ /app/features/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the tests
CMD ["behave"]
