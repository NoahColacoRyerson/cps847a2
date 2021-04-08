FROM ubuntu:latest

COPY ./public-html/ /var/www/html

EXPOSE 80/tcp
