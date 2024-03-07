ARG BASE=quay.io/jupyterhub/jupyterhub:4.0.2
FROM $BASE

RUN pip install --no-cache-dir --upgrade pip \
  pip install --no-cache-dir dockerspawner
