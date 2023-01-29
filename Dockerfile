FROM apache/superset:2.0.1

COPY ./docker/requirements.txt /app/requirements/

USER root

RUN pip install --no-cache -r /app/requirements/requirements.txt

USER superset