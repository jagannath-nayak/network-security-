FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required system packages including awscli
RUN apt-get update && \
    apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python3", "app.py"]
