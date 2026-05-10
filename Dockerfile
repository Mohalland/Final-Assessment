FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY source_code/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY source_code/ ./

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
