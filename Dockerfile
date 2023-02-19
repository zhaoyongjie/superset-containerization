FROM apache/superset:2.0.1

COPY ./docker/requirements.txt /app/requirements/

USER root

RUN pip install --no-cache -r /app/requirements/requirements.txt

USER superset

RUN cp -r /usr/local/lib/python3.8/site-packages/flask_appbuilder/static/appbuilder /app/superset/static
