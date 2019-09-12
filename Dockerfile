FROM python:3.7.4
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get install -y \
        nmap \
        vim

WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY . /
WORKDIR /app
