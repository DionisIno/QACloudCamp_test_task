FROM python:3.8-alpine
LABEL authors="Denis"

WORKDIR ./user
COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip install -r requirements.txt

CMD pytest -s -v tests/*