FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install requests

# Copy orchestrator code
COPY orchestrator.py /app/orchestrator.py

CMD ["python3", "orchestrator.py"]

