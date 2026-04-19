#!/usr/bin/env bash
# Export all .drawio files in docs/diagrams/ to PNG with embedded XML.
# Requires draw.io desktop app installed.

set -euo pipefail

DIAGRAMS_DIR="$(cd "$(dirname "$0")/../docs/diagrams" && pwd)"
SCALE="${1:-2}"

# Locate draw.io CLI
if command -v drawio &>/dev/null; then
  DRAWIO_CMD="drawio"
elif [ -f "/Applications/draw.io.app/Contents/MacOS/draw.io" ]; then
  DRAWIO_CMD="/Applications/draw.io.app/Contents/MacOS/draw.io"
elif [ -f "/mnt/c/Program Files/draw.io/draw.io.exe" ]; then
  DRAWIO_CMD="/mnt/c/Program Files/draw.io/draw.io.exe"
else
  echo "Error: draw.io CLI not found. Install the draw.io desktop app."
  exit 1
fi

echo "Using draw.io: $DRAWIO_CMD"
echo "Scale: ${SCALE}x"
echo "Directory: $DIAGRAMS_DIR"
echo ""

count=0
for drawio_file in "$DIAGRAMS_DIR"/*.drawio; do
  [ -f "$drawio_file" ] || continue
  png_file="${drawio_file}.png"
  echo "Exporting: $(basename "$drawio_file") → $(basename "$png_file")"
  "$DRAWIO_CMD" -x -f png -e -b 10 --scale "$SCALE" -o "$png_file" "$drawio_file"
  count=$((count + 1))
done

echo ""
echo "Done: $count diagram(s) exported."
