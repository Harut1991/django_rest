##Database creation
###For psql

    sudo su - postgres
    psql > DROP DATABASE IF EXISTS first;
    psql > CREATE DATABASE first;
    psql > CREATE USER first_user WITH password 'root';
    psql > GRANT ALL privileges ON DATABASE first TO first_user;
    psql > ALTER USER first_user CREATEDB;

    