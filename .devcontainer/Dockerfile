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

# Create a script to start Ollama
RUN echo '#!/bin/bash \n\
echo "Starting Ollama server" \n\
ollama serve &>/tmp/ollama.log & \n\
echo "Ollama server started" \n\
exec "$@"' > /usr/local/bin/entrypoint.sh && chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["bash"]
