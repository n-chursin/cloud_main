FROM python:3.9-alpine3.17

RUN apk update && \
    apk upgrade && \
    apk add --no-cache build-base

WORKDIR /app

COPY dependencies.txt . ./app

RUN pip install --no-cache-dir -r dependencies.txt

COPY app.py . ./app

CMD ["python3", "app.py"]