FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ="Europe/Moscow"

RUN mkdir --parents /usr/local/share/ca-certificates/Yandex/
RUN wget "https://storage.yandexcloud.net/cloud-certs/RootCA.pem" --output-document /usr/local/share/ca-certificates/Yandex/RootCA.crt
RUN wget "https://storage.yandexcloud.net/cloud-certs/IntermediateCA.pem" --output-document /usr/local/share/ca-certificates/Yandex/IntermediateCA.crt
RUN chmod 655 /usr/local/share/ca-certificates/Yandex/RootCA.crt && chmod 655 /usr/local/share/ca-certificates/Yandex/IntermediateCA.crt
RUN update-ca-certificates
RUN pip install poetry==1.4.0
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

COPY . .

EXPOSE 8000

CMD gunicorn main_api:app --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000