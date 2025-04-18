# Primary-Backup Replication Exercise

**Language:** Python

---

## Overview

In this exercise, you are provided with a fully implemented distributed key-value store demonstrating **primary-backup replication**. Your task is to:

1. Clone the repository and set up the environment on your local machine.  
2. Launch the provided servers and client.  
3. Execute the prescribed commands and simulate failure scenarios.  
4. Analyze the system’s behavior and write a detailed report.

## Repository Structure

- `primary.py`  — Primary server implementation
- `backup.py`   — Backup server implementation
- `client.py`   — CLI client for issuing GET/SET commands
- `test.sh`     — (Optional) script to automate basic tests
- `README.md`   — This file

## Prerequisites

- Python 3.7 or higher  
- UNIX-like shell (Linux/macOS) or Windows PowerShell

## Setup & Execution

1. **Clone** or download this repository.
2. Open three terminal windows or tabs:

   **Terminal 1: Start Backup Server**
   ```bash
   python3 backup.py --port 9001
   ```

   **Terminal 2: Start Primary Server**
   ```bash
   python3 primary.py --port 8000 --backups 127.0.0.1:9001
   ```

   **Terminal 3: Start Client**
   ```bash
   python3 client.py --port 8000
   ```

## Testing & Interaction

1. In the client terminal, run:
   ```bash
   SET key1 value1
   GET key1
   ```
2. Verify that the backup has the data:
   ```bash
   echo "DUMP" | nc 127.0.0.1 9001
   ```
3. (Optional) Execute automated tests:
   ```bash
   chmod +x test.sh
   ./test.sh
   ```

## Failure Scenarios

- **Simulate Backup Crash:**
  1. Stop the backup server (e.g., `Ctrl+C`).
  2. In the client terminal, perform `SET` and `GET` operations against the primary.
  3. Restart the backup and observe whether it synchronizes (check logs).

## Report Requirements

Submit a report (PDF or Markdown) covering:

1. **Introduction:** Describe primary-backup replication and its benefits.  
2. **Environment:** OS, Python version, and network configuration.  
3. **Execution Steps:** Commands executed, with screenshots or log excerpts.  
4. **Results:** Observations for normal operation and failure scenarios.  
5. **Analysis:** Discuss consistency, fault tolerance, and any limitations.  
6. **Recommendations:** Propose two improvements or alternative approaches.

Share a link to your report via the course portal.

## Grading Rubric

| Criterion                         | Weight |
|-----------------------------------|--------|
| Accuracy of setup & execution     | 30%    |
| Coverage of test scenarios        | 25%    |
| Depth and clarity of analysis     | 25%    |
| Organization and presentation     | 10%    |
| Practical recommendations         | 10%    |

---

*End of README.md*

