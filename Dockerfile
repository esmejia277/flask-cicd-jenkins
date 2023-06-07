FROM python:3.10.11-buster

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--access-logfile=-", "main:app"]