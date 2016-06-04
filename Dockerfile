FROM python:3.4-slim

RUN apt-get update && apt-get -y install \
    build-essential \
    curl \
    git \
    libpq-dev \
    vim


WORKDIR /var/app

COPY requirements.txt Makefile /var/app/

RUN make install

EXPOSE 5000

CMD ["make", "develop"]
