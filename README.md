Simple CLI Terminal (Python)

A simple command-line interface (CLI) application written in Python.
This project simulates a basic terminal with custom commands and JSON-based data storage.

🚀 Features
 • Command-based interface (like a real terminal)
 • Add, list and delete notes
 • Command history tracking
 • Current date and time display
 • Persistent data storage using JSON

🧠 Available Commands

help        - show all commands
exit        - exit the program
clear       - clear the screen

add   - add a new note
list        - show all notes
del     - delete note by index

date        - show current date
time        - show current time

history     - show command history

📁 Project Structure

simple-terminal/
│
├── main.py          # main loop and command handling
├── commands.py      # command implementations
├── commands.json    # data storage

⚙️ How It Works
 • Commands are mapped to functions using a dictionary
 • Data is stored in a JSON file
 • File paths are handled relative to the script location
 • Decorators are used to track command history

▶️ Run

python main.py

📌 Status

Project in progress.
Recent updates:
 • Added delete command
 • Added date and time commands
 • Implemented command history tracking

💡 Purpose

This project was created to practice:
 • Python fundamentals
 • File handling (JSON)
 • CLI application design
 • Code structuring and modularization