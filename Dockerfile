FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /work

WORKDIR /work


ADD /work/

ADD requirements.txt /work/

RUN pip install -r requirements.txt
