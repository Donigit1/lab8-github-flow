from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.panel import Panel

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return f"[bold green]You walk left.[/bold green] {random_event}"
    elif choice == "right":
        return f"[bold blue]You walk right.[/bold blue] {random_event}"
    else:
        return "[bold yellow]You stand still, unsure what to do. The forest swallows you.[/bold yellow]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print(Panel("[bold cyan]You wake up in a dark forest. You can go left or right.[/bold cyan]"))

    while True:
        choice = console.input("[bold white]Which direction do you choose? (left/right/exit): [/bold white] ")
        choice = choice.strip().lower()

        if choice == "exit":
            console.print("[bold red]You decide to leave the forest...[/bold red]")
            console.print("[bold green]Farewell, traveler! Until the next adventure! [/bold green]")
            break

        console.print(step(choice, events))
