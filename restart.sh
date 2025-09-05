#!/bin/bash

PROJECT_NAME="AdminBE"
PORT=9000
LOG_DIR="serverlogs"

# Create log directory if not exists
mkdir -p $LOG_DIR

# Generate log file name with date (e.g., server-2025-09-05.log)
LOG_FILE="$LOG_DIR/server-$(date +%Y-%m-%d).log"

# Kill any process running on the port
echo "🔍 Killing process on port $PORT (if any)..."
PID=$(lsof -t -i:$PORT)
if [ ! -z "$PID" ]; then
    kill -9 $PID
    echo "✅ Process $PID killed."
else
    echo "ℹ️  No process found on port $PORT."
fi

# Activate virtual environment (adjust path if needed)
echo "⚡ Activating virtual environment..."
source env/bin/activate

# Run makemigrations and migrate
echo "🛠️  Making migrations..."
python manage.py makemigrations >> $LOG_FILE 2>&1

echo "🛠️  Applying migrations..."
python manage.py migrate >> $LOG_FILE 2>&1

# Restart the server and log output
echo "🚀 Starting Django server on port $PORT..."
nohup python manage.py runserver 0.0.0.0:$PORT >> $LOG_FILE 2>&1 &

echo "✅ Django project restarted successfully on http://127.0.0.1:$PORT"
echo "📄 Logs: $LOG_FILE"
