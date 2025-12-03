# Python base image
FROM python:3.10-slim

# Create app directory
WORKDIR /app

# Install dependencies
RUN pip install flask

# Copy application code
COPY main.py /app/main.py

# Expose port
EXPOSE 8080

# Run the agent server
CMD ["python3", "main.py"]

