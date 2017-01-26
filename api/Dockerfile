FROM python:3
RUN apt-get update && apt-get install -y python-psycopg2 && apt-get autoremove -y
RUN pip install flask \
                psycopg2 \
                Flask-SQLAlchemy \
                Flask-Migrate \
                sqlalchemy \
                sqlalchemy-utils \
                alembic

WORKDIR /code

EXPOSE 5000

