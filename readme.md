# Django Docker
#### Dockerizing a Django app
---

# Containers
* Django : __python:alpine__
* Postgres : __postgres:latest__
* Nginx : __nginx__
* Redis : __redis:latest__
* Celery :  __python:alpine__
---
# How To Run
1. >create a .env file just like .env-simple
2. >sudo docker-compose up --build
---
# Celery Tasks
1. backup every 6hr
2. run task on route `http://localhost/addtask/?a=44&b=7&wait=3` __add a & b return result aflter -wait- seconds__
3. run task for sending email `http://localhost/email/` and return result
---
# Volumes
* ./nginx/gunicorn
* ./volumes/static
* ./volumes/media __create with django app (use for nginx container to serve)__
* ./volumes/dbdata
* ./volumes/celerydata