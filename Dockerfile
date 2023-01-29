FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /StyleTransfer

ADD . /StyleTransfer

RUN pip install -r requirements.txt

CMD ["python3",  "./main.py"]
