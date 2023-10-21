# Use the official image as a parent image
FROM python:3.9-slim-buster

# Set the working directory in docker
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the default command to run on container start
CMD ["bash"]