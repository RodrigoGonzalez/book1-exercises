# 7.6 review exercises

from random import randint


# Simulate the toss of a die
print(randint(1, 6))


# Simulate 10,000 throws of dice and display the average result
trials = 10000
total = sum(randint(1, 6) for _ in range(0, trials))
avg_result = total / trials
print(f"The average result of {trials} throws was {avg_result}")
