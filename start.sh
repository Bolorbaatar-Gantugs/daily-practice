#!/bin/bash
set -e

REPO_DIR="$HOME/daily-practice"

echo "=== ДАСГАЛ ЭХЛҮҮЛЭХ ==="
read -p "Хэлний төрөл (bash, python, java...) [bash]: " CATEGORY
CATEGORY="${CATEGORY:-bash}"

read -p "Дасгалын нэр [task]: " TASK_INPUT
TASK_INPUT="${TASK_INPUT:-task}"

TODAY=$(date "+%Y-%m-%d")
BASE_DIR="$REPO_DIR/$CATEGORY/$TODAY"
mkdir -p "$BASE_DIR"

TARGET_DIR="$BASE_DIR/$TASK_INPUT"
COUNT=2

while [ -d "$TARGET_DIR" ]; do
    TARGET_DIR="${BASE_DIR}/${TASK_INPUT}_${COUNT}"
    COUNT=$((COUNT + 1))
done

mkdir -p "$TARGET_DIR"
echo "$TARGET_DIR" > "$REPO_DIR/.current_task"

echo "--------------------------------------------------"
echo "✅ Ажиллах талбар бэлэн: $TARGET_DIR"
echo "--------------------------------------------------"
