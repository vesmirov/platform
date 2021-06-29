FROM python:3.8.6

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code

CMD gunicorn blog.wsgi:application -b 0:8000
ENTRYPOINT ["./entrypoint.sh"]
