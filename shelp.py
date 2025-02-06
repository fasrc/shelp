#!/usr/bin/env python3

import os

# List of Slurm commands and their descriptions (including custom commands)
commands = [
    ("squeue", "Show jobs in the queue."),
    ("sbatch", "Submit a job script."),
    ("salloc", "Allocate resources for a job in real-time."),
    ("srun", "Run a job within an allocation."),
    ("scancel", "Cancel jobs or job steps."),
    ("scontrol", "Manage or query job/system states."),
    ("sinfo", "Display information about nodes and partitions."),
    ("sreport", "Generate reports from Slurm accounting."),
    ("sacct", "Display job accounting data."),
    ("sacctmgr", "Manage accounting data for jobs/users."),
    ("spart", "Show partitions you have access to."),
    ("showq", "Display cluster state."),
    ("scalc", "Perform various Slurm calculations (e.g., fairshare usage)."),
    ("find-best-partition", "See which partition will schedule your job the quickest."),
]

# Define color codes for better legibility
RED = "\033[1;31m"
GREEN = "\033[1;32m"
NC = "\033[0m"  # No Color

# Function to display Slurm commands with aligned descriptions
def show_menu():
    print(f"{GREEN}Select a Slurm command to get more information:{NC}")
    max_command_len = max(len(command) for command, _ in commands)
    for i, (command, description) in enumerate(commands, start=1):
        print(f"{RED}{i:>2}.{NC} {GREEN}{command:<{max_command_len}}{NC} {description}")
    print(f"{RED} 0.{NC} Exit")

# Function to display help or custom message for a given command
def display_help(command):
    custom_commands = {
        "spart": "spart: Show partitions you have access to.",
        "showq": "showq: Display cluster state.",
        "scalc": "scalc: Perform various Slurm calculations such as projected fairshare usage.",
        "find-best-partition": "find-best-partition: See which partition will schedule your job the quickest.",
    }

    if command in custom_commands:
        print(custom_commands[command])
    else:
        # Display --help for standard Slurm commands
        os.system(f"{command} --help | less")

        # Ask if the user wants to see the man page
        show_man = input(f"Would you like to see the man page for '{command}'? (y/n): ").strip().lower()
        if show_man == "y":
            os.system(f"man {command}")

# Main loop
def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter the number of the command (or 0 to exit): ").strip())
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        if choice == 0:
            print("Exiting...")
            break
        elif 1 <= choice <= len(commands):
            command = commands[choice - 1][0]
            display_help(command)
            print(f"\n{GREEN}Select another Slurm command or press Ctrl-C to quit.{NC}")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
