# 8.6.2 coin_toss.py
# Simulate the results of a series of coin tosses and track the results

from random import randint

flips = 0
trials = 10000

for _ in range(0, trials):
    flips += 1  # first flip
    if randint(0, 1) == 0:  # flipped tails on first flip
        while randint(0, 1) == 0:  # keep flipping tails
            flips += 1
    else:  # otherwise, flipped heads on first flip
        while randint(0, 1) == 1:  # keep flipping heads
            flips += 1
    flips += 1  # finally flipped heads
print(flips / trials)
