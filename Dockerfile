FROM python:3.9

RUN mkdir -p /usr/myapp

WORKDIR /usr/myapp

ADD . /usr/myapp

CMD ["python", "app.py"]