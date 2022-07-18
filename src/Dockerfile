# syntax=docker/dockerfile:1
FROM python:3.10.5-alpine

# Disable python buffering and bytecode *.pyc compiling. 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project directory.
WORKDIR /srv/www/florgon/ads-api

# Install requirements.
COPY ads-api/requirements.txt /srv/www/florgon/ads-api/
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Copy whole project.
COPY . /srv/www/florgon/ads-api/

# Run project.
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]