FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD Password1234
ENV POSTGRES_DB books-crud

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
