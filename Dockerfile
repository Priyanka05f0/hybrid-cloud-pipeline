FROM python:3.11

WORKDIR /app

COPY src/bridge.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "bridge.py"]