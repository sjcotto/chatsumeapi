FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PORT 8080
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

RUN pip install pipenv spacy
COPY ./requirements/requirements.txt ./requirements/requirements.txt
CMD pipenv shell
RUN pipenv lock --requirements > requirements/requirements.txt
RUN pip install -r requirements/requirements.txt
RUN python3 -m spacy download en_core_web_sm

COPY ./app /app/app