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

pull_required_model() {
  # Get model from env var or use default
  local MODEL="${OLLAMA_MODEL:-llama3.2}"

  log "Checking if model '$MODEL' is already available..."
  if ! curl -s "${BASE_URL}/api/tags" | grep -q "\"${MODEL}\""; then
    log "Model '$MODEL' not found. Pulling now (this may take a while)..."
    curl -s "${BASE_URL}/api/pull" -d "{\"model\":\"${MODEL}\", \"stream\":false}"
    if [ $? -eq 0 ]; then
      log "✅ Model '$MODEL' successfully pulled"
    else
      log "⚠️ Failed to pull model '$MODEL'. You may need to pull it manually."
      log "Try: curl http://localhost:11434/api/pull -d '{\"model\":\"${MODEL}\"}'"
    fi
  else
    log "✅ Model '$MODEL' is already available"
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

  # Pull the model needed for auto-descriptions
  pull_required_model

  log "✅ Ollama is successfully running and ready to use"
  MODEL="${OLLAMA_MODEL:-llama3.2}"
  log "You can use it with: curl http://localhost:11434/api/generate -d '{\"model\":\"${MODEL}\",\"prompt\":\"Hello\"}'"
}

main "$@"
