import random

import numpy as np
import matplotlib.pyplot as plt
from core.Blob import Blob, TYPES

from core.events.day import day

NUM_DAYS = 100
NUM_POP = 5


def night(current_pop: int):
    pop_update = np.random.randint(1, 2 + 1, current_pop).sum()
    return pop_update


def main():
    pop = [Blob(id, 0) for id in range(0, NUM_POP)]
    pop_hist = [0] * NUM_DAYS
    pop_hist[0] = len(pop)
    die_hist = [0] * NUM_DAYS
    reproduction_hist = [0] * NUM_DAYS

    for i in range(1, NUM_DAYS):
        cur_pop_size = len(pop)
        pop = day(pop)
        death_amount = cur_pop_size - len(pop)
        if len(pop) == 0:
            die_hist[i] = death_amount
            reproduction_hist[i] = 0
            pop_hist[i] = 0
            break
        die_hist[i] = pop_update
        pop_update = night(pop)
        pop += pop_update
        reproduction_hist[i] = pop_update
        pop_hist[i] = pop

    draw_stats(pop_hist)


def draw_stats(pop_hist: [int]):
    plt.plot(pop_hist)
    plt.show()


if __name__ == '__main__':
    main()
