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

# Devcontainer setup
RUN apt-get install -y \
    bash \
    man \
    neovim \
    netcat \
    sudo
RUN curl -fsSL https://get.docker.com | sh -

# Add the dist to the sudoers
RUN echo 'dist ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers

# Script to allow non-root access to the docker.sock file
# https://github.com/microsoft/vscode-dev-containers/tree/main/containers/docker-from-docker-compose
COPY ./.devcontainer/entrypoint.sh /usr/local/share/entrypoint.sh
RUN chmod +x /usr/local/share/entrypoint.sh
ENTRYPOINT [ "/usr/local/share/entrypoint.sh" ]
