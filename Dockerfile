# Base Python:3.10 slim
FROM python:3.10-slim

# Expose port 5000
EXPOSE 5000/tcp

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages from pipfile
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# Run res.py when the container launches
CMD ["python", "./res.py"]