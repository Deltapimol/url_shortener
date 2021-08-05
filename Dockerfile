FROM python:3.7
COPY requirements.txt .
USER root
ENV PYTHONUNBUFFERED 1
RUN pip install --user -r requirements.txt

WORKDIR /url_shortener
COPY . /url_shortener

