import random

from core.Blob import Blob
from core.config import PROB_BIRTH, ID_COUNTER


def night(pop: [Blob]):
    n_offsprings = random.choices(population=[0, 1, 2], weights=PROB_BIRTH, k=len(pop))
    for i, n_o in enumerate(n_offsprings):
        pop.extend([Blob(next(ID_COUNTER), pop[i].type) for _ in range(0, n_o)])
    return pop