FROM python:3.6-slim

WORKDIR /usr/app

RUN apt update -y
RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD ./src .

CMD ["python", "-u", "-m", "main"]
