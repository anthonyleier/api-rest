FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN pip install psycopg2==2.9.3 flask==2.1.2 flask_restful==0.3.9

ENTRYPOINT ["/usr/local/bin/python"]