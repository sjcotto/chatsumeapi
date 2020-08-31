FROM python:3.7

COPY ./requirements/requirements.txt ./requirements/requirements.txt
RUN pip3 install -r requirements/requirements.txt
RUN python3 -m spacy download en_core_web_sm

COPY ./app /app
RUN useradd -m myuser
USER myuser





CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]