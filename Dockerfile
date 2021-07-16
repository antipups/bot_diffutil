FROM python:latest

COPY . /bot_diffutil

WORKDIR /bot_diffutil

ENV ip_address="185.255.135.27"

RUN pip install -r requirements.txt && \
    sed -i "s/\.\.\./$ip_address/" bot/websocket.py && \
    openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out bot/pub_key.crt -keyout bot/priv_key.key -subj "/C=RU/ST=Moscow/L=Moscow/O=./OU=./CN=$ip_address"


ENTRYPOINT ["python", "main.py"]