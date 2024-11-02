FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
COPY Server.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "Server.py"]

EXPOSE 8080