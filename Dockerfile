FROM PYTHON:3.10 

ENV PYTHONUNBUFFERED=1

WORKDIR /CODE

COPY requirements.txt .

COPY . .

EXPOSE 8000

CMD ["python3","manage.py","runserver"]