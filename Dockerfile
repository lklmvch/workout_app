# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt ./


# Copy the rest of the application code
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
