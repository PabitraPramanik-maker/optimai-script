# optimai-script
# OptimAI Multi-Node Auto Ref Script

**RAJA RX SCRIPT** — A Python-based multi-node dashboard and auto referral simulator for OptimAI.

## Features
- Supports multiple accounts (access tokens)
- Assigns separate proxies per node
- Colorful terminal output with status, points, and rate tracking
- Easily configurable via `tokens.txt` and `proxies.txt`

## Requirements
- Python 3.7+
- `rich` and `pyfiglet` packages (install via `pip install rich pyfiglet`)

## Setup
1. Create `tokens.txt` and add one access token per line.
2. Create `proxies.txt` and add one HTTP proxy per line (e.g., `http://123.45.67.89:8080`).
3. Run the script:

```bash
python optimx.py
