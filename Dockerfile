FROM python:3.7.7-alpine
COPY . /app
WORKDIR /app
RUN pipenv install
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 
