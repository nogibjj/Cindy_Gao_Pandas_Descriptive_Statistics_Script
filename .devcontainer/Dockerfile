# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/codespaces-linux/.devcontainer/base.Dockerfile
# Dockerfile allows the developer to automate the process of setting up an environment by specifying the base image,
# installing dependencies, copying files, setting environment variables, and defining the commands that should run
# when the container starts.
FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal

# Dockerfile is a text file that contains a set of instructions used to create a Docker image. #

RUN apt-get update && apt-get -y install --no-install-recommends \
   python3.8-venv \
   gcc 
   
ARG USER="codespace"
ARG VENV_PATH="/home/${USER}/venv"
COPY requirements.txt /tmp/
COPY Makefile /tmp/
RUN su $USER -c "/usr/bin/python3 -m venv /home/${USER}/venv" \
   && su $USER -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt" \
   && rm -rf /tmp/requirements.txt 
