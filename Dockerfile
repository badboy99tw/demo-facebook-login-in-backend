FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_DEBUG=1
ENTRYPOINT flask run --host=0.0.0.0
