import random
from collections import Counter

import numpy as np

from core.Blob import Blob

NUM_TREES = 100
PROB_OF_PREDATOR = 0.5
TREES = np.repeat(range(0, NUM_TREES), 2).tolist()


def day(pop: [Blob]):
    random.shuffle(pop)
    if len(pop) > NUM_TREES:
        pop = pop[:NUM_TREES]
    selected_tree = random.sample(TREES, len(pop))
    predator_occurrence = np.random.random(NUM_TREES) < PROB_OF_PREDATOR
    new_pop = []
    for i in range(0, len(pop)):
        if not (predator_occurrence[selected_tree[i]]):
            new_pop.append(pop[i])
    return new_pop
