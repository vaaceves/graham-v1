FROM python:3.6
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /webapps
    WORKDIR /webapps
    # Installing OS Dependencies
    RUN apt-get update && apt-get upgrade -y
    RUN apt-get install -y swig libssl-dev dpkg-dev netcat libsqlite3-dev
    RUN apt-get -y install ffmpeg
    RUN pip install -U pip setuptools
    COPY requirements.txt /webapps/
    COPY requirements-opt.txt /webapps/
    RUN pip install -r /webapps/requirements.txt
    ADD . /webapps/
# Django service
EXPOSE 8000
RUN chown -R $USER:$USER /webapps/*
RUN chown -R $USER:$USER .