FROM python:3.8-alpine
LABEL authors="Denis"

WORKDIR ./app
VOLUME /allure_result
RUN apk update && apk upgrade && apk add bash
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD pytest -s -v --alluredir=allure_result tests/*