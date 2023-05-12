FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .
COPY requirements_dev.txt .

RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]