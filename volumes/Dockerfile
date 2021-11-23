FROM python:alpine

ENV PYTHONDONTWRITEBYTHECODE 1
ENV PYTHONNUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN apk update
RUN apk add --no-cache postgresql-libs gcc musl-dev postgresql-dev

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN apk del postgresql-libs gcc musl-dev postgresql-dev

RUN mkdir -p /run/gunicorn
#celery dirs
RUN mkdir -p /var/run/celery
RUN mkdir -p /var/log/celery

CMD while ! python3 manage.py sqlflush > /dev/null 2>&1 ; do sleep 1 ; done && \
    python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL} --noinput ; \
    #gunicorn -b 0.0.0.0:8000 djangodocker.wsgi
    #celery -A djangodocker worker --beat -l info
    gunicorn --workers ${GUNICORN_WORKER} --bind unix:/run/gunicorn/gunicorn.sock djangodocker.wsgi
