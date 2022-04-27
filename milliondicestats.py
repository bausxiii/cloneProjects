"""Million Dice Roll Statistics Simulator,
A simulation of one million dice rolls.

Tags: tiny, beginner, math, simulation"""

import random
import time

print('''Million Dice Roll Statistics Simulator,

Enter how many six-sided dice you want to roll:''')
numberOfDice = int(input('> '))

# Set up a dictionary to store the results of each dice roll:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Simulate dice rolls:
print(f'Simulating 1,000,000 rolls of {numberOfDice} dice...')
lastPrintTime = time.time()

for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print(f'{round(i / 10000, 1)}% done...')
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)

    results[total] += 1

# Display results:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(f'  {i} - {roll} - {percentage}%')
