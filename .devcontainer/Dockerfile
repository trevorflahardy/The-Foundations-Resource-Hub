FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y git build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    pip install --no-cache-dir pyright

CMD ["bash"]
