FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN python -m pip install Django
COPY . /app

ENTRYPOINT python manage.py runserver 0.0.0.0:8000 