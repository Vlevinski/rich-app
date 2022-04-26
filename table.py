#!/usr/bin/env python

from rich.console import Console
from rich.table import Table

table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

console = Console()
console.print(table)


