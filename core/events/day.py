import random
from collections import Counter

import numpy as np

from core.Blob import Blob
from core.config import NUM_TREES, TREES, PROB_OF_PREDATOR, T_ALT, T_COW, T_IMP, T_SUC, PROB_ALTRUIST_DIES, GREEN_BEARD, \
    POPULATION_SIMULATION


def day(pop: [Blob]):
    # only certain amount of available trees, others randomly die
    random.shuffle(pop)
    if len(pop) > 2 * NUM_TREES:
        pop = pop[:2 * NUM_TREES]

    predator_occurrence = np.random.random(NUM_TREES) < PROB_OF_PREDATOR
    agents_at_tree = [[] for _ in range(NUM_TREES)]  # create different lists

    # each agent picks one of the 2 available places of each tree
    selected_tree = random.sample(TREES, len(pop))
    for i_agent, i_tree in enumerate(selected_tree):
        agents_at_tree[i_tree].append(i_agent)
    new_pop = []
    for i in range(0, NUM_TREES):
        # if no predator, agents at that tree live on
        if not (predator_occurrence[i]):
            new_pop.extend([pop[i_agent] for i_agent in agents_at_tree[i]])
        else:
            # basic setup
            if POPULATION_SIMULATION:
                continue
            # mechanics for different types
            elif len(agents_at_tree[i]) == 2:  # if only one, it gets eaten
                eat_order = [0, 1]
                random.shuffle(eat_order)
                i_eaten = agents_at_tree[i][eat_order[0]]
                i_survi = agents_at_tree[i][eat_order[1]]

                agent_survi = pop[i_survi]
                agent_eaten = pop[i_eaten]
                if agent_survi.type == T_ALT or agent_survi.type == T_SUC:
                    # if only alt, help everyone or if alt green, help only other alt green or impostor
                    if (not GREEN_BEARD or agent_survi.type == T_SUC) or (
                            agent_eaten.type == T_ALT or agent_eaten.type == T_IMP):
                        # originally eaten one survives when altruist yells
                        new_pop.append(pop[i_eaten])
                        if np.random.random() > PROB_ALTRUIST_DIES:
                            # probability that altruist survives too
                            new_pop.append(pop[i_survi])
                    else:
                        # altruist didn't yell and survives
                        new_pop.append(pop[i_survi])
                elif agent_survi.type == T_COW or agent_survi.type == T_IMP:
                    new_pop.append(pop[i_survi])
    return new_pop
