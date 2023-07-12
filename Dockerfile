FROM python:3.8-buster

# Docker内での作業ディレクトリ指定
WORKDIR /workspace/
COPY requirements.txt /workspace/

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y default-jre default-jdk \
 && pip install -r requirements.txt