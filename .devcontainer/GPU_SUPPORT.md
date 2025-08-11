# GPU Support for Ollama in DevContainer

This document explains how GPU acceleration works in the Arduino Guide development container.

## How GPU Support is Enabled

The development container is configured to automatically detect and use NVIDIA GPUs when available:

1. The devcontainer.json contains `"runArgs": ["--gpus=all"]` to pass GPU devices to the container
2. The Dockerfile installs the NVIDIA Container Toolkit
3. The entrypoint script checks for GPU availability and configures Ollama accordingly
4. Environment variables `NVIDIA_VISIBLE_DEVICES` and `NVIDIA_DRIVER_CAPABILITIES` are set

## Requirements on Host Machine

To use GPU acceleration, your host machine must have:

1. An NVIDIA GPU with up-to-date drivers installed
2. NVIDIA Container Toolkit (nvidia-docker2) installed
3. Docker configured to use the NVIDIA runtime

## Verifying GPU Support

After starting the container, GPU support can be verified with:

```bash
# Run the included GPU check script
./.devcontainer/scripts/check_gpu.sh

# Or check manually with these commands
nvidia-smi  # Should show GPU information
curl http://localhost:11434/api/tags  # Check Ollama GPU support
```

## Troubleshooting

If GPU acceleration isn't working:

1. Check that NVIDIA drivers are properly installed on the host
2. Verify NVIDIA Container Toolkit is installed: `nvidia-container-cli info`
3. Make sure Docker is configured to use the NVIDIA runtime
4. Check Ollama logs: `cat /tmp/ollama.log`

## For macOS Users (Apple Silicon)

This configuration is designed for NVIDIA GPUs. For Apple Silicon (M1/M2/M3) Macs:

1. The NVIDIA-specific configuration will be ignored
2. Ollama will automatically use Metal for acceleration on Apple Silicon
3. No additional configuration is needed for Apple Silicon GPUs
