FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Set environment variables to avoid buffering and enable Flask debug if needed
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production


CMD ["python", "app.py"]
