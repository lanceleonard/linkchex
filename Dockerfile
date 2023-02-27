FROM python:latest

WORKDIR /app

# Use apt-get to avoid warnings; can use apt, but there will be warnings.
RUN apt-get update && apt-get install nano

# Pull requirements into the container and then install them.
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY src ./src
