FROM tensorflow/tensorflow:2.15.0-gpu

WORKDIR /app

COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/live_trading.py"]