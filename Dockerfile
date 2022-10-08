FROM python:latest
 RUN apt-get update
 
 RUN mkdir project
 WORKDIR project
 COPY requirements.txt .
 RUN pip3 install -r requirements.txt
  
 COPY / ./