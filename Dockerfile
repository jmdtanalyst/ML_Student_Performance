FROM python:3.9
WORKDIR /app
COPY . /app

RUN apt update -y

RUN pip install -r requirements.txt

CMD ["python3","app.py"]