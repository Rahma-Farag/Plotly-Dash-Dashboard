FROM python:latest
 RUN apt-get update
 
 RUN mkdir Plotly-Dash-Dashboard
 WORKDIR Plotly-Dash-Dashboard
 COPY requirements.txt .
 RUN pip3 install -r requirements.txt
  
 COPY . ./
 RUN python app.py