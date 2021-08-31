FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED=1

WORKDIR /full_django

COPY requirements.txt /full_django/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /full_django/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]