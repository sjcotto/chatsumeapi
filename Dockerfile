FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PORT 8080
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

COPY ./requirements/requirements.txt ./requirements/requirements.txt
RUN pip install -r requirements/requirements.txt

COPY ./app /app/app 
