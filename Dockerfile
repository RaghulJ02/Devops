FROM python:3.8-slim

WORKDIR /app

COPY app.py /app
COPY house_price_model.pkl /app

RUN pip install flask scikit-learn

EXPOSE 5000

CMD ["python", "app.py"]
