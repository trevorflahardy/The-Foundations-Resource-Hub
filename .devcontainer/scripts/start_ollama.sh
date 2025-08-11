#!/bin/bash
set -euo pipefail

BASE_URL="${OLLAMA_URL:-http://localhost:11434}"

log() { echo "[ollama-startup] $*"; }

start_ollama_server() {
  if ! pgrep -x "ollama" > /dev/null; then
    log "Starting Ollama server..."
    nohup ollama serve > /tmp/ollama.log 2>&1 &
    sleep 2
    log "Ollama server started in background"
  else
    log "Ollama server is already running"
  fi
}

wait_for_server() {
  local retries=30
  local i=0
  log "Waiting for Ollama service at ${BASE_URL}..."
  until curl -sf "${BASE_URL%/}/api/tags" >/dev/null 2>&1; do
    i=$((i+1))
    if [ "$i" -ge "$retries" ]; then
      log "Timed out waiting for Ollama at ${BASE_URL}"
      return 1
    fi
    if [ "$((i % 5))" -eq 0 ]; then
      log "Still waiting for Ollama service... (${i}/${retries})"
    fi
    sleep 1
  done
  log "✅ Ollama is up and running at ${BASE_URL}"
}

main() {
  # First try to start the Ollama server
  start_ollama_server

  # Then wait for it to be ready
  wait_for_server || {
    log "Ollama server failed to start properly. Checking logs..."
    if [ -f "/tmp/ollama.log" ]; then
      log "Last 10 lines of Ollama logs:"
      tail -n 10 /tmp/ollama.log
    fi
    exit 1
  }

  log "✅ Ollama is successfully running and ready to use"
  log "You can use it with: curl http://localhost:11434/api/generate -d '{\"model\":\"llama3.2\",\"prompt\":\"Hello\"}'"
}

main "$@"
