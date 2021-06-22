import random

import numpy as np
import matplotlib.pyplot as plt
from core.Blob import Blob, TYPES
from core.config import NUM_POP, NUM_DAYS, PROB_BIRTH, NUM_SIMULATIONS

from core.events.day import day


def night(pop: [Blob]):
    birth_rate = np.sum(random.choices(population=[0, 1, 2], weights=PROB_BIRTH, k=len(pop)))
    pop.extend([Blob(id, 0) for id in range(0, birth_rate)])
    return pop


def simulation():
    pop = [Blob(id, 0) for id in range(0, NUM_POP)]
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
    return pop_hist


def main():
    pop_histories = [0] * NUM_SIMULATIONS
    for i in range(0, NUM_SIMULATIONS):
        pop_hist = simulation()
        pop_histories[i] = pop_hist
        plt.plot(pop_hist, color='grey', linewidth=0.2)

    # AVG
    avg_hist = np.mean(pop_histories, axis=0)
    draw_stats(avg_hist)

def draw_stats(pop_hist: [int]):
    plt.plot(pop_hist)
    plt.ylabel('population')
    plt.xlabel('days')
    plt.show()


if __name__ == '__main__':
    main()
