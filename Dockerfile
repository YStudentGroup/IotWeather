# Dockerfile

FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "SimulateData.py"]
