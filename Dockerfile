FROM python:3

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/src

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN flake8 /app/src