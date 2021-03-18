# DOCKERFILE FOR CALLBACK
FROM python:3.7 
RUN pip install Flask gunicorn requests

COPY requirements.txt .
# install dependencies files 
RUN pip install -r requirements.txt 

COPY src/ app/ 
COPY config.json .
COPY private_key.json .

WORKDIR /app 

# update
RUN apt-get update

ENV PORT 8080 

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app 