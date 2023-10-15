FROM python:3.10 

ENV PYTHONUNBUFFERED=1

WORKDIR /CODE

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3","manage.py","runserver"]