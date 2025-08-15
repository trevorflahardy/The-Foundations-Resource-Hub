FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git build-essential curl procps ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Install Python requirements for docs and CLI
COPY requirements.txt /tmp/
COPY rst_to_html/requirements.txt /tmp/rst_to_html_requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    pip install --no-cache-dir -r /tmp/rst_to_html_requirements.txt && \
    pip install --no-cache-dir pyright

# Install Ollama (simple method for single container)
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the Ollama startup script
COPY .devcontainer/scripts/start_ollama.sh /usr/local/bin/start_ollama.sh
RUN chmod +x /usr/local/bin/start_ollama.sh

# No custom entrypoint - will use the default CMD
CMD ["bash"]
