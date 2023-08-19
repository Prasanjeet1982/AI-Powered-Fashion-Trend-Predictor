# Use the official Python image as the base image
FROM python:3.8

# Set environment variables for Python and ensure output is unbuffered
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
