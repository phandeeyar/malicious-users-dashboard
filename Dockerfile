FROM python:3.8.0
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' appuser
COPY --chown=appuser:appuser . /code/