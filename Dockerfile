FROM python:3.10-alpine

RUN apk update && \
    apk add --no-cache gcc libc-dev linux-headers postgresql-dev nano

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENV APP_NAME=anitiming
CMD gunicorn -w 3 --chdir . web.wsgi --bind 0.0.0.0:8000