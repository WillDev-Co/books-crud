FROM python:3.9-slim-buster

WORKDIR /app

COPY api.py /app/api.py
COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]

