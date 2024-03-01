FROM postgres:latest
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=gaming_store_db
WORKDIR /my_DB
COPY . /my_DB
EXPOSE 5432
COPY ./init.sql /docker-entrypoint-initdb.d/
env 