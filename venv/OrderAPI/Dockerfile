# Dockerfile, Image, Container

# Base image of python version 3.8
FROM python:3.8

# Working directory for upcoming commands
WORKDIR /order-app

# Copies requirement.txt file
COPY requirements.txt .

# Runs python command to install libraries in requirement file
RUN pip install -r requirements.txt

# Copies the DATA subdirectory
COPY DATA data

# Launching python script
CMD ["python", "OrderAPI/DATA/orderapp.py"]