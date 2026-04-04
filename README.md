# Simple Terminal CLI (Python)

A simple command-line terminal application written in Python with custom commands and JSON-based storage.

## Features

- Add and manage notes
- Edit notes by index
- Delete single or all notes
- Search notes (find command)
- Show current date and time
- Command history tracking
- Backup system for saving data copies
- Clear terminal screen

## Commands

help        - show available commands  
add <text>  - add a new note  
list        - show all notes  
del <id>    - delete note by index  
edit <id> <text> - edit note  
find <text> - search notes  
count       - show number of notes  
del_all     - delete all notes (with confirmation)  
date        - show current date  
time        - show current time  
history     - show command history  
backup      - create backup file  
clear       - clear terminal  
exit        - exit application  

## Storage

All data is stored in a JSON file:
- commands.json

Backups are automatically saved as:
- commands1.json, commands2.json, etc.

## How to Run

1. Install Python
2. Run:

python main.py

## Project Structure

main.py       - main loop and command handling  
commands.py   - all command functions  
commands.json - data storage  

## Future Improvements

- Executable (.exe) version
- Better command parsing
- UI improvements
- More advanced commands

---

This project was created as a practice for working with:
- CLI applications
- JSON storage
- File system operations
- Python architecture