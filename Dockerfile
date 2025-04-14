# Dockerfile
FROM python:3.11-slim 


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (optional for prod)
RUN python manage.py collectstatic --noinput

# Run with Gunicorn (production server)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
