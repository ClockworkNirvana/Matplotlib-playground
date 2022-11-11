import matplotlib.pyplot as plt
import numpy as np
import random

simulations = 100000
jumps = 5
probability = 0.707


def cycle_modified(trials, probs):
    done = 0
    lefts = 0
    while done != trials:
        rand_num = random.random()
        if done == 0:
            if rand_num > 0.5:
                lefts += 1
        else:
            if rand_num < probs:
                lefts += 1
        done += 1
    return lefts


def data_gen(sims, trials, probs):
    data = [0] * (trials + 1)
    i = 0
    while i != sims:
        consider = cycle_modified(trials, probs)
        data[trials-consider] += 1
        i += 1
    return [x/sims for x in data]


x_data = list(range(1, jumps+2))
y_data = data_gen(simulations, jumps, probability)
fig = plt.figure(figsize=(10, 5))

plt.bar(x_data, data_gen(simulations, jumps, probability))

plt.xlabel("Position")
plt.ylabel("Probability")
plt.suptitle("Probability distribution of the jumper landing on a given position from the left")
plt.title("P(jumps left) = {}, Num of jumps = {}, P(jump left on 1st jump) = {}".format(probability, jumps, 0.5))
plt.show()
