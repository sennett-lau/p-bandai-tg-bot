FROM python:3.10-alpine
RUN apt-get update -y
COPY app /app
WORKDIR /app
RUN pip install -r ./requirements.txt
CMD [ "python", "./main.py" ]
