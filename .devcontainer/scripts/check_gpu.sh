#!/bin/bash
set -euo pipefail

log() { echo "[gpu-check] $*"; }

log "Checking for NVIDIA GPU support..."

# Try nvidia-smi to see if we have GPU access
if command -v nvidia-smi &> /dev/null; then
    log "NVIDIA GPU detected:"
    nvidia-smi --query-gpu=name,memory.total,memory.free,driver_version --format=csv

    # Check CUDA availability for PyTorch
    log "Testing CUDA availability with Python:"
    python -c "
import torch
if torch.cuda.is_available():
    print(f'✓ CUDA is available: {torch.cuda.device_count()} device(s)')
    print(f'✓ Current device: {torch.cuda.get_device_name(0)}')
else:
    print('✗ CUDA is not available')
" 2>/dev/null || log "PyTorch test failed (torch may not be installed)"

    # Check Ollama CUDA access
    log "Checking if Ollama can access GPU:"
    curl -s http://localhost:11434/api/tags | grep -q "CUDA" && log "✓ Ollama has GPU support" || log "✗ Ollama doesn't appear to be using GPU"
else
    log "No NVIDIA GPU detected or container doesn't have GPU access."
    log "If you have an NVIDIA GPU on the host, make sure:"
    log "1. NVIDIA Container Toolkit is installed on the host"
    log "2. Docker is configured to use NVIDIA runtime"
    log "3. The container is run with --gpus flag"
fi

log "GPU check complete"
