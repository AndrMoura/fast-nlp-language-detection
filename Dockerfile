FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends \
    g++ \
    protobuf-compiler \
    libprotobuf-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt  .
RUN pip install -r requirements.txt


COPY . .

RUN chmod +x run.sh

EXPOSE 9612

CMD ./run.sh