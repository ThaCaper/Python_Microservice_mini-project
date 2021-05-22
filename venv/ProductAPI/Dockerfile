# Dockerfile, Image, Container
FROM python:3.8

WORKDIR /product-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./DATA ./productapi

CMD ["python", "./DATA/productapp.py"]