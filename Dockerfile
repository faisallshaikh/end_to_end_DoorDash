FROM python:3.9-slim-buster 
WORKDIR /app
COPY requirements.txt .
COPY . /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "web_flask.py"]


