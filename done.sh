#!/bin/bash
set -e

if [ ! -f .current_task ]; then
    echo "❌ Алдаа: Идэвхтэй дасгал олдсонгүй! Эхлээд ./start.sh ажиллуулна уу."
    exit 1
fi

ACTIVE_DIR=$(cat .current_task)
TASK_NAME=$(basename "$ACTIVE_DIR")
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "[$TIMESTAMP] Дууссан: $ACTIVE_DIR" >> progress.log

git add .
git commit -m "Completed: $ACTIVE_DIR ($TIMESTAMP)" || true
git push origin main 2>/dev/null || git push origin master 2>/dev/null || true

rm -rf "$ACTIVE_DIR"
rm -f .current_task

echo "--------------------------------------------------"
echo "✅ $ACTIVE_DIR бүртгэгдэж, GitHub руу илгээгдлээ!"
echo "🧹 Түр хавтас ($ACTIVE_DIR) цэвэрлэгдэж 0 боллоо."
echo "--------------------------------------------------"
