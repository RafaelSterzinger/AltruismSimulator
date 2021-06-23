import itertools
import os
import random
from _operator import add

import numpy as np
import matplotlib.pyplot as plt

from core import config
from core.Blob import Blob, TYPES
from core.config import NUM_POP, NUM_DAYS, PROB_BIRTH, NUM_SIMULATIONS, TIME_STR, POP_TYPES, ID_COUNTER, POP_COLORS

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
    blob_hist = [0] * NUM_DAYS
    blob_hist[0] = pop

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
        blob_hist[i] = pop
        config.NUM_PASSED_NIGHTS += 1
    return blob_hist


# TODO move to seperate experiment yaml/config file (not config.py)
PLOT_RELATIVE = True


def separate_by_type(pop_hist):
    pop_hists_by_type = {type: [] for type in POP_TYPES.keys()}
    for agent_list in pop_hist:
        counts = {type: 0 for type in POP_TYPES.keys()}
        for agent in agent_list:
            counts[agent.type] += 1

        for type, count in counts.items():
            pop_hists_by_type[type].append(count)

    return pop_hists_by_type


def main():
    blob_histories = [0] * NUM_SIMULATIONS
    count_histories_dict = {type: [[] for _ in range(NUM_SIMULATIONS)] for type in POP_TYPES.keys()}
    for i in range(0, NUM_SIMULATIONS):
        reset_environment()
        blob_hist = simulation()
        blob_histories[i] = blob_hist
        count_hist_dict = separate_by_type(blob_hist)
        for k, v in count_hist_dict.items():
            count_histories_dict[k][i] = v

        plot_dict_by_color(count_hist_dict, linewidth=0.1)

        # TODO visualize stacked lineplot, add type 0 to 1 for the second
        # maybe create two plots, one with absolute counts and one with percentages
        # as the prior would not show well having both lines

    # AVG
    avg_hist = {k: np.mean(v, axis=0) for k, v in count_histories_dict.items()}
    draw_stats(avg_hist)


def plot_dict_by_color(count_hists_by_type_dict, linewidth=1.0, fill=False):
    offset_count_hist = [0] * NUM_DAYS
    for type, count_hist_by_type in count_hists_by_type_dict.items():
        temp = list(map(add, offset_count_hist, count_hist_by_type))
        if fill:
            plt.fill_between(range(NUM_DAYS), offset_count_hist, temp, color=POP_COLORS[type], alpha=0.2)
        plt.plot(temp, color=POP_COLORS[type], linewidth=linewidth)
        offset_count_hist = temp




def reset_environment():
    config.NUM_PASSED_NIGHTS = 0
    config.ID_COUNTER = itertools.count()


def draw_stats(pop_hist: [int]):
    plot_dict_by_color(pop_hist, linewidth=1.0, fill=True)
    plt.ylabel('population')
    plt.xlabel('days')
    filepath = 'report/figures/archive/'
    os.makedirs(filepath, exist_ok=True)
    plt.savefig(f'{filepath}{TIME_STR}.pdf')
    plt.show()


if __name__ == '__main__':
    main()
