# Primary-Backup Replication System

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)

## Overview

This repository contains a distributed key-value store demonstrating the **primary-backup replication** pattern, a fundamental concept in distributed systems. The system consists of three main components:

- **Primary Server**: Handles client requests and replicates data to the backup
- **Backup Server**: Stores replicated data and promotes itself to primary on failure detection
- **Client**: Provides a simple interface for users to interact with the system

This implementation showcases important distributed systems concepts including:
- Data replication for fault tolerance
- Leader election via heartbeat failure detection
- Consistency preservation in distributed state

## Repository Structure

- [`primary.py`](https://github.com/darshjoshi/primary-backup-replication/blob/main/primary.py) - Primary server implementation that processes client requests and replicates data
- [`backup.py`](https://github.com/darshjoshi/primary-backup-replication/blob/main/backup.py) - Backup server that stores replicated data and monitors primary health
- [`client.py`](https://github.com/darshjoshi/primary-backup-replication/blob/main/client.py) - Client application for interacting with the distributed key-value store
- [`common.py`](https://github.com/darshjoshi/primary-backup-replication/blob/main/common.py) - Shared utilities for network communication
- [`config.py`](https://github.com/darshjoshi/primary-backup-replication/blob/main/config.py) - System configuration (ports, timeouts, etc.)

## How It Works

1. **Normal Operation:**
   - Primary server accepts client requests (GET/SET operations)
   - For SET operations, the primary:
     - Updates its local store
     - Replicates the change to the backup server
     - Acknowledges success to the client
   - Primary sends regular heartbeats to the backup

2. **Failure Handling:**
   - If the backup stops receiving heartbeats from the primary, it promotes itself to primary
   - The new primary continues to serve client requests
   - When original primary comes back online, it needs to be reconfigured as a backup

## Prerequisites

- Python 3.7 or higher
- UNIX-like terminal (macOS/Linux) or Windows PowerShell
- Network connectivity between components (all run locally by default)

## Installation

```bash
# Clone this repository
git clone https://github.com/darshjoshi/primary-backup-replication.git
cd primary-backup-replication

# No additional dependencies required - just standard Python libraries
```

## Configuration

The default configuration in `config.py` uses the following ports:
- Primary server: Port 8000 (localhost)
- Backup server: Port 9001 (localhost)

If these ports are already in use on your system, you can modify them in the `config.py` file.

## Running the System

You need to run each component in the correct order in separate terminal windows:

### 1. Start the Backup Server

```bash
# In Terminal 1
python3 backup.py
```

You should see: `[BACKUP] Listening for primary on localhost:9001`

### 2. Start the Primary Server

```bash
# In Terminal 2
python3 primary.py
```

You should see: `[PRIMARY] Listening on localhost:8000`

NOTE: The primary must be started shortly after the backup (within the heartbeat timeout window), otherwise the backup will promote itself to primary.

### 3. Start the Client

```bash
# In Terminal 3
python3 client.py
```

The client will display a prompt: `>> Commands: SET <key> <value> | GET <key> | EXIT`

## Using the System

Once all components are running, you can interact with the system through the client interface:

### Basic Operations

```
>> SET color blue
-> {'status': 'OK'}

>> GET color
-> {'status': 'OK', 'value': 'blue'}

>> SET count 42
-> {'status': 'OK'}

>> GET count
-> {'status': 'OK', 'value': '42'}

>> GET nonexistent
-> {'status': 'OK', 'value': None}
```

### Verifying Replication

To verify that data has been replicated to the backup server, you can use the netcat (`nc`) utility to request a data dump:

```bash
# In a new terminal window
echo "DUMP" | nc 127.0.0.1 9001
```

This should display all key-value pairs currently stored in the backup server.

## Testing Failure Scenarios

### Simulating Primary Failure

1. Set up the system with all three components running
2. Set some values using the client
3. Kill the primary server with Ctrl+C
4. Observe the backup server's logs - it should detect the failure and promote itself
5. The promoted backup should now be able to handle client requests

### Simulating Backup Failure

1. Set up the system with all three components running
2. Set some values using the client
3. Kill the backup server with Ctrl+C
4. Continue to set and get values through the client
5. The primary server will report connection errors to the backup but continue to operate
6. Restart the backup server and observe whether it synchronizes with the primary

## Troubleshooting

### Port Already in Use

If you see an error like `OSError: [Errno 48] Address already in use`, it means another process is using the configured port. You can either:

1. Terminate the conflicting process:
   ```bash
   lsof -i :8000,9001  # Find processes using these ports
   kill -9 <PID>       # Kill the process using the relevant port
   ```

2. Or modify the port numbers in `config.py`.

### Backup Automatically Promotes to Primary

If the backup server automatically promotes itself to primary immediately after starting, this means:

1. Either the primary server isn't running, or
2. The heartbeat timeout is too short

In a production system, you would configure a longer timeout to avoid false positives. For testing, ensure you start the primary server quickly after starting the backup.

## Implementation Details

### Heartbeat Mechanism

The system uses a simple heartbeat mechanism:
- Primary sends periodic heartbeats to the backup every `HEARTBEAT_INTERVAL` seconds (default: 2 seconds)
- If the backup doesn't receive a heartbeat for `HEARTBEAT_TIMEOUT` seconds (default: 30 seconds), it assumes the primary has failed and promotes itself

### Data Consistency

This implementation follows a simple consistency model:
- Writes are acknowledged only after replication to the backup
- No sophisticated conflict resolution mechanism is implemented
- If the backup is unavailable, the primary continues to operate (availability over consistency)

## Future Improvements

1. **Multi-Backup Support**: Extend the system to support multiple backup servers for increased fault tolerance
2. **Dynamic Node Discovery**: Add a mechanism for servers to discover each other automatically
3. **Data Persistence**: Add disk-based storage to survive complete system restarts
4. **Conflict Resolution**: Implement vector clocks or other mechanisms for conflict detection and resolution
5. **Client-Side Load Balancing**: Allow clients to auto-discover and connect to the current primary

## License

This project is available for educational purposes.

## Acknowledgments

This implementation was created as a teaching tool to demonstrate basic distributed systems concepts.

---

*Last updated: April 18, 2025*
