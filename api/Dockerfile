FROM python:3
RUN apt-get update && apt-get install -y python-psycopg2 && apt-get autoremove -y
ADD . /api
WORKDIR /api

RUN pip install -r ./requirements.txt 

WORKDIR /code

EXPOSE 5000

