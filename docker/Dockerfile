FROM python:3.11

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME='/usr/local' \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

ENV POETRY_VERSION=1.2.2

RUN apt-get update \
    && apt-get install -qq -y curl make build-essential gcc libxext6 libsm6 xvfb xdg-utils wget unzip ffmpeg libpq-dev vim libmagick++-dev fonts-liberation sox bc gsfonts --no-install-recommends\
    && apt-get clean

## ImageMagicK Installation 
RUN mkdir -p /tmp/distr && \
    cd /tmp/distr && \
    wget https://download.imagemagick.org/ImageMagick/download/releases/ImageMagick-7.0.11-2.tar.xz && \
    tar xvf ImageMagick-7.0.11-2.tar.xz && \
    cd ImageMagick-7.0.11-2 && \
    ./configure --enable-shared=yes --disable-static --without-perl && \
    make && \
    make install && \
    ldconfig /usr/local/lib && \
    cd /tmp && \
    rm -rf distr

RUN curl -sSL https://install.python-poetry.org | python3 -

USER root

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root

COPY . .