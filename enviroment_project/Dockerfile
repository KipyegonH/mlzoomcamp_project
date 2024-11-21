# 1. Start with a base image that includes Python
FROM python:3.8-slim

RUN pip install pipenv
COPY . /app
WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system
COPY ["predict.py","xgb_model.pkl", "dv.pkl", "./"]

EXPOSE 9696


CMD ["python", "predict.py"]
