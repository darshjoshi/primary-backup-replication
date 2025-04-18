# config.py

# Network configuration
PRIMARY_HOST = 'localhost'
PRIMARY_PORT = 8000  # Changed from 5000 to avoid conflicts

BACKUP_HOST = 'localhost'
BACKUP_PORT = 9001  # Changed from 5001 to avoid conflicts

# Heartbeat settings (in seconds)
HEARTBEAT_INTERVAL = 2
HEARTBEAT_TIMEOUT = 30  # Increased from 5 to give us more time
