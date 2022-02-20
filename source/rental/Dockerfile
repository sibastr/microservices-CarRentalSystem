FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /source
COPY requirements.txt /source
RUN pip install -r requirements.txt
COPY . /source
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:$PORT



