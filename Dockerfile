FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /users
WORKDIR /users
ADD . /users/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage_prod.py makemigrations && python manage_prod.py migrate && python manage_prod.py runserver 0.0.0.0:$PORT