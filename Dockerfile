FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

USER root

EXPOSE 80

CMD ["python", "app.py"]
