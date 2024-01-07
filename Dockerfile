FROM python:3.9-slim-buster
WORKDIR /app
COPY . /aap
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "web_flask.py"]