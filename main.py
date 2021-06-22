import itertools
import os
import random

import numpy as np
import matplotlib.pyplot as plt

from core import config
from core.Blob import Blob, TYPES
from core.config import NUM_POP, NUM_DAYS, PROB_BIRTH, NUM_SIMULATIONS, TIME_STR, POP_TYPES, ID_COUNTER

from core.events.day import day

NUM_PASSED_NIGHTS = "ERROR: ONLY ACCESS BY config.py AS VARIABLE GETS CHANGED"


def night(pop: [Blob]):
    n_offsprings = random.choices(population=[0, 1, 2], weights=PROB_BIRTH, k=len(pop))
    for i, n_o in enumerate(n_offsprings):
        # TODO: enable that one can have offspring of different type than oneself (similar to above weights with a shift)
        pop.extend([Blob(next(ID_COUNTER), pop[i].type) for _ in range(0, n_o)])
    return pop


def simulation():
    types = []
    for type, percentage in POP_TYPES.items():
        types.extend(np.repeat(type, percentage * NUM_POP))
    pop = [Blob(next(ID_COUNTER), types[id]) for id in range(0, NUM_POP)]
    pop_hist = [0] * NUM_DAYS
    pop_hist[0] = len(pop)
    die_hist = [0] * NUM_DAYS
    reproduction_hist = [0] * NUM_DAYS
    for i in range(1, NUM_DAYS):
        cur_pop_size = len(pop)

        pop = day(pop)
        death_rate = cur_pop_size - len(pop)
        if len(pop) == 0:
            die_hist[i] = death_rate
            reproduction_hist[i] = 0
            pop_hist[i] = 0
            break
        die_hist[i] = death_rate

        cur_pop_size = len(pop)
        pop = night(pop)
        birth_rate = len(pop) - cur_pop_size
        reproduction_hist[i] = birth_rate

        pop_hist[i] = len(pop)
        config.NUM_PASSED_NIGHTS += 1
    return pop_hist


def main():
    pop_histories = [0] * NUM_SIMULATIONS
    for i in range(0, NUM_SIMULATIONS):
        reset_environment()
        pop_hist = simulation()
        pop_histories[i] = pop_hist
        plt.plot(pop_hist, color='grey', linewidth=0.2)
        # TODO visualize stacked lineplot, add type 0 to 1 for the second
        # maybe create two plots, one with absolute counts and one with percentages
        # as the prior would not show well having both lines

    # AVG
    avg_hist = np.mean(pop_histories, axis=0)
    draw_stats(avg_hist)


def reset_environment():
    config.NUM_PASSED_NIGHTS = 0
    config.ID_COUNTER = itertools.count()


def draw_stats(pop_hist: [int]):
    plt.plot(pop_hist)
    plt.ylabel('population')
    plt.xlabel('days')
    filepath = 'report/figures/archive/'
    os.makedirs(filepath, exist_ok=True)
    plt.savefig(f'{filepath}{TIME_STR}.pdf')
    plt.show()


if __name__ == '__main__':
    main()
