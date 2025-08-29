# Use the official Python image as a base
FROM python:3.9-slim

# Install build tools needed for dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the function code and dependencies file
COPY lambda_function.py .
COPY requirements.txt .

# Install Python dependencies
# We install torch without CUDA support for a smaller image size
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run when the container starts
CMD [ "lambda_function.lambda_handler" ]
