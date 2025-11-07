import random
import copy
import time
import sys

"""
Conway's Game of Life

A simple implementation of Conway's Game of Life that runs in the
terminal. It generates a random initial state and then prints
successive generations.
"""

rows = 80
columns = 20
dead = ' '  # Character for a dead cell
alive = '0'  # Character for an alive cell

# Create a dictionary to store the grid state.
# Keys are (x, y) tuples, values are 'dead' or 'alive'.
nextIteration = {}

# Initialize the First Grid
# Loop through every cell and assign a random state.
for x in range(rows):
    for y in range(columns):
        if random.randint(0, 1) == 0:
            nextIteration[(x, y)] = alive
        else:
            nextIteration[(x, y)] = dead

# Wrap the main loop in a try/except to catch Ctrl+C
try:
    # Main Program Loop
    while True:

        # "Clear" the screen by printing 50 newlines
        print('\n' * 50)

        # Make a deep copy of the grid.
        # 'iteration' is the state for this loop's calculation.
        # 'nextIteration' is what we will build for the *next* loop.
        # This prevents changes from affecting the current calculation.
        iteration = copy.deepcopy(nextIteration)

        # Display the Current Grid
        for y in range(columns):
            for x in range(rows):
                # 'end=''' prevents print from adding a newline after each cell
                print(iteration[(x, y)], end='')
            print()  # Print a newline at the end of each row

        print('Hit Ctrl + C to exit')

        # Calculate the Next Generation
        # Loop through every cell in the grid
        for x in range(rows):
            for y in range(columns):

                # Calculate coordinates for all 8 neighbors
                # The modulo (%) operator makes the grid "wrap around"
                left = (x - 1) % rows
                right = (x + 1) % rows
                above = (y - 1) % columns
                below = (y + 1) % columns

                # Count Living Neighbors
                neighbours = 0
                if iteration[(left, above)] == alive:
                    neighbours += 1
                if iteration[(x, above)] == alive:
                    neighbours += 1
                if iteration[(right, above)] == alive:
                    neighbours += 1
                if iteration[(left, y)] == alive:
                    neighbours += 1
                if iteration[(right, y)] == alive:
                    neighbours += 1
                if iteration[(left, below)] == alive:
                    neighbours += 1
                if iteration[(x, below)] == alive:
                    neighbours += 1
                if iteration[(right, below)] == alive:
                    neighbours += 1

                # Apply Conway's Game of Life Rules
                # A living cell with 2 or 3 living neighbors stays alive
                if iteration[(x, y)] == alive and (neighbours == 2 or neighbours == 3):
                    nextIteration[(x, y)] = alive
                # A dead cell with 3 living neighbors becomes alive
                elif iteration[(x, y)] == dead and neighbours == 3:
                    nextIteration[(x, y)] = alive
                # All other cells die or stay dead
                else:
                    nextIteration[(x, y)] = dead

        # Pause for 1 second before drawing the next iteration
        time.sleep(1)

except KeyboardInterrupt:
    # Runs if Ctrl+C is pressed at any time
    print("\nConway's Game of Life - Exiting.")
    sys.exit()  # Exit the program