"""Conway's Game of Life,
The classic cellular automata simulation. Press Ctrl-C to stop.
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Tags: short, artistic, simulation, dictionaries"""


import copy
import random
import sys
import time

# Set up constants:
WIDTH = 79      # The width of the cell grid.
HEIGHT = 20     # The height of the cell grid.

ALIVE = '#'  # (!) Try changing to '#' or another character '|'.
DEAD = ' '   # (!) Try changing to '.' or another character '-'.

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
nextCells = {}

# Put random dead and alive cells into nextCells:
for x in range(WIDTH):          # Loop over every possible column.
    for y in range(HEIGHT):     # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE  # Add a living cell.
        else:
            nextCells[(x, y)] = DEAD  # Add a dead cell.

while True:  # Main program loop.
    # Each iteration of this loop is a step of the simulation.

    print('\n' * 50)  # Seperate each step of the simulation.

    # Deep copy from copy module...
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # Print the # or space.
        print()
    print('Print Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they
            # wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:   # Top-left neighbor
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:      # Top neighbor
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:  # Top-right neighbor
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:       # Left neighbor
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:      # Right neighbor
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:   # Bottom-left neighbor
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:      # Bottom neighbor
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:  # Bottom-right neighbor
                numNeighbors += 1

            # Set cell based on Conway's Game of Life RULES:
            if (cells[(x, y)] == ALIVE and (numNeighbors == 2
                or numNeighbors == 3)):
                # Living cells with 2 or 3 neighbor stay alive:
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()  # When Ctrl-C is pressed, end the program.


# PATTERNS
# Still lifes
# Oscillators
# Spaceships

# Add some functions...
'''glider = {}  # before glider empty grid...

glider[(0, 0)] = DEAD
glider[(1, 0)] = DEAD
glider[(2, 0)] = DEAD
glider[(3, 0)] = DEAD
glider[(4, 0)] = DEAD
glider[(0, 1)] = DEAD
glider[(1, 1)] = DEAD
glider[(2, 1)] = DEAD
glider[(3, 1)] = ALIVE
glider[(4, 1)] = DEAD
glider[(0, 2)] = DEAD
glider[(1, 2)] = DEAD
glider[(2, 2)] = DEAD
glider[(3, 2)] = DEAD
glider[(4, 2)] = ALIVE
glider[(0, 3)] = DEAD
glider[(1, 3)] = DEAD
glider[(2, 3)] = ALIVE
glider[(3, 3)] = ALIVE
glider[(4, 3)] = ALIVE
glider[(0, 4)] = DEAD
glider[(1, 4)] = DEAD
glider[(2, 4)] = DEAD
glider[(3, 4)] = DEAD
glider[(4, 4)] = DEAD

glider = {(0, 0): 'A',
             (1, 0): DEAD,
             (2, 0): DEAD,
             (3, 0): DEAD,
             (4, 0): DEAD,
             (0, 1): DEAD,
             (1, 1): DEAD,
             (2, 1): DEAD,
             (3, 1): ALIVE,
             (4, 1): DEAD,
             (0, 2): DEAD,
             (1, 2): DEAD,
             (2, 2): DEAD,
             (3, 2): DEAD,
             (4, 2): ALIVE,
             (0, 3): DEAD,
             (1, 3): DEAD,
             (2, 3): ALIVE,
             (3, 3): ALIVE,
             (4, 3): ALIVE,
             (0, 4): DEAD,
             (1, 4): DEAD,
             (2, 4): DEAD,
             (3, 4): DEAD,
             (4, 4): DEAD,}'''
