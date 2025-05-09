# AIE Devcontainer Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.10

# Install Node.js, npm, and Smithery CLI for MCP
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    npm install -g @smithery/cli && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python tools
RUN pip install --upgrade pip && \
    pip install black flake8 pytest
