FROM python:3.8

ENV DJANGO_SETTINGS_MODULE project.settings
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y unzip wget
RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1


WORKDIR /code
COPY . /code/
RUN ls -a
RUN pip install -r requirements.txt