import time
import random
import threading
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

def banner():
    text = pyfiglet.figlet_format("R A J A  R X  S C R I P T", font="standard")
    banner_text = Text(text, style="bold yellow on green")
    console.print(Panel(banner_text, style="green"), justify="center")

def load_file(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print(f"[red]File not found: {filename}[/red]")
        return []

class Node:
    def __init__(self, node_id, proxy):
        self.node_id = node_id
        self.proxy = proxy
        self.points = random.randint(1000, 5000)
        self.connected = True
        self.increase_rate = random.uniform(0.1, 5.0)

    def simulate_activity(self):
        if self.connected:
            self.points += self.increase_rate * random.uniform(0.8, 1.2)

class Account:
    def __init__(self, name, token, proxies):
        self.name = name
        self.token = token
        self.nodes = []
        # Create 7 nodes per account with different proxies
        for i in range(7):
            proxy = proxies[i % len(proxies)] if proxies else None
            self.nodes.append(Node(f"Node-{i+1}", proxy))

    def update_nodes(self):
        for node in self.nodes:
            node.simulate_activity()

def display_accounts(accounts):
    console.clear()
    banner()
    for acc in accounts:
        table = Table(title=f"[bold cyan]{acc.name}[/bold cyan]", expand=True, show_lines=True, border_style="green")
        table.add_column("Node ID", style="bold yellow")
        table.add_column("Proxy", style="magenta")
        table.add_column("Connected", justify="center")
        table.add_column("Points", justify="right")
        table.add_column("Increase Rate / min", justify="right")

        for node in acc.nodes:
            connected_str = "[green]Yes[/green]" if node.connected else "[red]No[/red]"
            points_str = f"{node.points:.2f}"
            rate_str = f"{node.increase_rate:.2f}"
            table.add_row(node.node_id, node.proxy or "None", connected_str, points_str, rate_str)

        console.print(table)
        console.print()

def main():
    tokens = load_file("tokens.txt")
    proxies = load_file("proxies.txt")

    if not tokens:
        console.print("[red]No access tokens found. Please add tokens in tokens.txt[/red]")
        return

    accounts = []
    for idx, token in enumerate(tokens):
        acc_name = f"Account-{idx+1}"
        accounts.append(Account(acc_name, token, proxies))

    while True:
        for acc in accounts:
            acc.update_nodes()

        display_accounts(accounts)
        time.sleep(60)  # Update every 60 seconds

if __name__ == "__main__":
    main()
