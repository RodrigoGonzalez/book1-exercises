from random import randint


def single_trial():
    toss = randint(0, 1)
    total_flips = 1

    while toss == randint(0, 1):
        total_flips += 1
        toss = randint(0, 1)

    total_flips += 1
    return total_flips


def flip_trial_avg(num_trials):
    total = sum(single_trial() for _ in range(num_trials))
    return total / num_trials

print("The average number of coin flips was {0}".format(flip_trial_avg(10000)))
