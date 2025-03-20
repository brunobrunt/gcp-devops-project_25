# Use the official Python image
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt requirements.txt

# Install dependencies
# Use RUN for build-time tasks (e.g., installing dependencies).
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . . 

# Expose Flask's default port
EXPOSE 5000

# Run the Flask app
# Use CMD for runtime commands (e.g., starting a Flask app).

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
