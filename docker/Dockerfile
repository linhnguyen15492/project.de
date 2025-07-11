FROM apache/airflow:latest


COPY requirements.txt /

USER root

RUN apt-get update && apt-get install -y gnupg software-properties-common && \
    curl -fsSL https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - && \
    add-apt-repository 'deb https://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main' && \
    apt-get update && \
    apt-get install -y mongodb-org-tools

USER airflow

RUN pip install -r /requirements.txt

CMD [ "standalone" ]