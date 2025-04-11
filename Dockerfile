FROM python:3.10.17-slim

# Update pip to the latest version
RUN python -m pip install --upgrade pip

# Update setuptools to the latest version
RUN pip install -U setuptools

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Run the command to start the app
ENTRYPOINT ["python", "main.py"]