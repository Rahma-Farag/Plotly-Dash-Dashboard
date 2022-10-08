FROM python:latest
RUN apt-get update

RUN mkdir Plotly-Dash-Dashboard
WORKDIR Plotly-Dash-Dashboard
COPY requirments.txt .
RUN pip3 install -r requirments.txt

COPY . ./
EXPOSE 8050
RUN python app.py