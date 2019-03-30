#### Demo use of Firebase Admin SDK with Django

Setup

Tools that you need to install:
* Django
* Celery
* RabbitMQ
* Redis
* Firebase Admin SDK

Steps to run:

1. Install the requirements.\
 `pip install -r requirements.txt`
 
2. Make and run migrations.\
   `python manage.py makemigrations`\
   `python manage.py runmigrations`\
   
3. Start the server.\
   `python manage.py runserver`
   
4. Start the Celery worker.\
   `celery -A messaging worker --loglevel=info`




 