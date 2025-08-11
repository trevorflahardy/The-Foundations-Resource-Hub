#!/bin/bash
set -euo pipefail

BASE_URL="${OLLAMA_URL:-http://localhost:11434}"

log() { echo "[ollama-startup] $*"; }

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
  wait_for_server || exit 1
  log "Container is ready to use"
}

main "$@"
