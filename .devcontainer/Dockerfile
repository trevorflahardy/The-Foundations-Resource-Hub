FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y git build-essential curl procps ca-certificates gnupg && \
    rm -rf /var/lib/apt/lists/*

# Install NVIDIA Container Toolkit for GPU support
RUN distribution=$(. /etc/os-release;echo $ID) && \
    curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && \
    curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
    apt-get update && apt-get install -y nvidia-container-toolkit && \
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

# Set environment variables for Ollama GPU detection
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Create a script to check for and enable GPU
RUN echo '#!/bin/bash \n\
if command -v nvidia-smi &> /dev/null; then \n\
    echo "NVIDIA GPU detected, enabling GPU for Ollama" \n\
    export CUDA_VISIBLE_DEVICES=0 \n\
    export OLLAMA_HOST=0.0.0.0 \n\
else \n\
    echo "No NVIDIA GPU detected, running in CPU mode" \n\
fi \n\
ollama serve &>/tmp/ollama.log & \n\
echo "Ollama server started" \n\
exec "$@"' > /usr/local/bin/entrypoint.sh && chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["bash"]
