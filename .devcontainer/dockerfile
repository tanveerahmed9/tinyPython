# Use the official Python image as a base
FROM python:3.9

# Install necessary tools and dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    unzip \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install Azure Functions Core Tools
RUN wget -q https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y azure-functions-core-tools-4

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Python packages
RUN pip install --no-cache-dir azure-functions azure-cosmos azure-storage-blob azure-cognitiveservices-vision-computervision

# Set the working directory
WORKDIR /workspace

# Keep the container running
CMD ["bash"]