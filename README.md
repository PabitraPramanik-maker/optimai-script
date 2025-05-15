# OptimAI Multi-Node Auto Referral Script  
**RAJA RX SCRIPT** — A Python-based multi-node dashboard and auto referral simulator for OptimAI.

## Features

- Supports multiple accounts with access tokens  
- Assigns separate proxies per node  
- Colorful terminal output showing status, points, and increase rate  
- Easy configuration via `tokens.txt` and `proxies.txt`  
- Auto detects nodes and manages connections

## Requirements

- Python 3.7 or higher  
- Install required packages: `pip install rich pyfiglet`

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/PabitraPramanik-maker/optimai-script.git
```bash
   cd optimai-script
   ```

2. **Install Requirements:**
   ```bash
   pip install rich pyfiglet

   ```

## Configuration

- **tokens.txt: Add your OptimAI access tokens, one per line:
  ```bash
   your_access_token_1
   your_access_token_2
   your_access_token_3

  ```

- **proxy.txt:** You will find the file `proxy.txt` inside the project directory. Make sure `proxy.txt` contains data that matches the format expected by the script. Here are examples of file formats:
  ```bash
    ip:port # Default Protcol HTTP.
    protocol://ip:port
    protocol://user:pass@ip:port
  ```

## Run

```bash
python optimx.py

```
---

If you found this project helpful, please ⭐ **Star** the repository on GitHub! It really helps us grow and improve. Thank you! 🙌

