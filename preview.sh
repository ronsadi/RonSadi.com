#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-8080}"

python3 marketplace_crawler.py > mvp-output.txt

echo "Generated mvp-output.txt from marketplace_crawler.py"
echo "Starting local preview server on http://localhost:${PORT}"
echo "Press Ctrl+C to stop"
python3 -m http.server "${PORT}"
