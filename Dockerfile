FROM python:latest

WORKDIR /app

# Use apt-get to avoid warnings; can use apt, but there will be warnings.
RUN apt-get update && apt-get install nano sqlite3
RUN pip install --upgrade pip


# Pull requirements into the container and then install them.
ADD requirements.txt . 
RUN pip install -r requirements.txt

ADD src ./src

#
CMD ["src/run"] 