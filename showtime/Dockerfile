FROM python:3.9-alpine3.13
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app/
CMD ["python","-u","server.py"]
