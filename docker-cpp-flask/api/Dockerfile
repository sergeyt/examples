FROM docker

RUN apk update \
    && apk add --no-cache python3 \
    && pip3 install pipenv \
    && pip3 install gunicorn

COPY . /app

WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["./main.sh"]
