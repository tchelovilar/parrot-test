FROM python:3.8-alpine

ENV FLASK_APP=/app/run.py

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY src /app

EXPOSE 5000

CMD [ "python", "-u", "-m", "flask", "run", "--host=0.0.0.0" ]
