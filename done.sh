#!/bin/bash
set -e

REPO_DIR="$HOME/daily-practice"

if [ ! -f "$REPO_DIR/.current_task" ]; then
    echo "❌ Алдаа: Идэвхтэй дасгал олдсонгүй! Эхлээд start-practice ажиллуулна уу."
    exit 1
fi

ACTIVE_DIR=$(cat "$REPO_DIR/.current_task")
TASK_NAME=$(basename "$ACTIVE_DIR")
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

cd "$REPO_DIR"

echo "[$TIMESTAMP] Дууссан: $ACTIVE_DIR" >> progress.log

git add .
git commit -m "Completed: $ACTIVE_DIR ($TIMESTAMP)" || true
git push origin main 2>/dev/null || git push origin master 2>/dev/null || true

rm -rf "$ACTIVE_DIR"
rm -f "$REPO_DIR/.current_task"

echo "--------------------------------------------------"
echo "✅ $ACTIVE_DIR бүртгэгдэж, GitHub руу илгээгдлээ!"
echo "🧹 Түр хавтас цэвэрлэгдэж 0 боллоо."
echo "--------------------------------------------------"
