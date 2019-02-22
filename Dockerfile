

from alpine:latest

WORKDIR /app
COPY . /app

RUN apk add --no-cache python3-dev 
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
    && pip3 install --upgrade pip \
    





RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["parse_json.py"]