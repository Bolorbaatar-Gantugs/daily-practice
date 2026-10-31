#!/bin/bash
set -e

CATEGORY="${1:-general}"
TASK_INPUT="${2:-task}"

TODAY=$(date "+%Y-%m-%d")
BASE_DIR="$CATEGORY/$TODAY"
mkdir -p "$BASE_DIR"

TARGET_DIR="$BASE_DIR/$TASK_INPUT"
COUNT=2

while [ -d "$TARGET_DIR" ]; do
    TARGET_DIR="${BASE_DIR}/${TASK_INPUT}_${COUNT}"
    COUNT=$((COUNT + 1))
done

mkdir -p "$TARGET_DIR"
echo "$TARGET_DIR" > .current_task

echo "--------------------------------------------------"
echo "✅ Ангилал: [$CATEGORY] | Ажиллах талбар: $TARGET_DIR"
echo "👉 Орох команд: cd $TARGET_DIR"
echo "--------------------------------------------------"
