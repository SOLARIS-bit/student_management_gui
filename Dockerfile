# Use a slim Python base image
FROM python:3.11-slim

# Install Tkinter dependencies
RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Optional: install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "main.py"]
