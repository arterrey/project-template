# syntax=docker/dockerfile:1
FROM python:3.11-bullseye
RUN apt update -y

# Application dependencies
RUN apt install -y \
    build-essential \
    git \
    git-lfs \
    libpq-dev \
    libxml2-dev \
    libxslt-dev \
    pkg-config \
    postgresql-client \
    python-dev \
    zlib1g-dev

# Upgrade package installers
RUN pip install -U pip setuptools

# Add users
RUN groupadd dist
RUN useradd --gid dist --create-home --shell /bin/bash dist
RUN useradd --gid dist --create-home --shell /bin/bash proc

# Copy application across
COPY . /main
WORKDIR /main
RUN chown -R dist:dist /main

# Build
USER dist:dist
RUN bin/build
RUN find . -type f -iname *.py -exec bin/python -m py_compile {} \;

# Set permissions
USER root
RUN chown -R proc:dist var
RUN chmod -R u+rwX,g+Xr,g-w,o-rwx .

# Set run context
USER proc
