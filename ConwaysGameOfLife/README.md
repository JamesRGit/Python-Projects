# Conway's Game of Life (Terminal)
A simple Python script that runs John Horton Conway's "Game of Life" in the terminal.

What is Conway's Game of Life?

The Game of Life, also known as Conway's Game of Life or simply Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

This project initializes a random grid of living (`0`) and dead ` `) cells and then repeatedly applies the game's rules to show how the patterns evolve over time.

## Preview
The output will look something like this, with the pattern changing every second:
```bash
000    0               00                 000000        00000
   0 00                                      00 00       00
 00  00    0000           0000    000      00  00         00
00    0     00            0000    0000     00             000
00 000                   00       00        000          0
  00 0                                     000000
00  00                  000000
  00                    000000
                                 0000           00      00
00000                    000       00           00      00
 00                      000       000000      0000000  00000
  00000          000      00       00    00     00    00  00
   00000         000               00    00     00    00   00
    00 00        000        00000  000000       0000000    000
     00 00                  00000     00           00
       000                          00 00         00
      00 00                        00  00
     00  00        00000            00000
    00   00        00000
   00    00
Hit Ctrl + C to exit
```

## Features
- Start: Generates a random initial state for an 80x20 grid.
- Terminal Based: Runs directly in your terminal.
- Wraparound Grid: The grid edges wrap around (a "toroidal array"), so cells on the right edge are neighbors with cells on the left edge.
- Configurable: You can easily change the `rows` and `columns` variables at the top of the script to adjust the grid size.

Requirements
- Python 3.x 

No external libraries are needed, as the script only uses built-in modules (`random`, `copy`, `time`, `sys`).

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the directory containing the Python file.
```bash
cd path/to/your/project/folder
```

Run the script using Python:
```bash
# Replace 'your_script_name.py' with the actual file name
python your_script_name.py
```

## Controls
- **Start**: The game begins automatically.
- **Exit**: Press `Ctrl+C` to stop the program.
