FROM python:3.11

RUN mkdir /telegram_api
WORKDIR /telegram_api

RUN pip install --upgrade pip
COPY requirements.txt /telegram_api/

RUN pip install -r requirements.txt
COPY . /telegram_api/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]