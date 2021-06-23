import random
from collections import Counter

import numpy as np

from core.Blob import Blob
from core.config import NUM_TREES, TREES, PROB_OF_PREDATOR, T_ALT, PROB_ALTRUIST_DIES, ALTRUISTS_ARE_EGOISTS


def day(pop: [Blob]):
    # only certain amount of available trees, others randomly die
    random.shuffle(pop)
    if len(pop) > NUM_TREES:
        pop = pop[:NUM_TREES]

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
        # altruism and cowardice logic
        else:
            if len(agents_at_tree[i]) == 2:  # if only one, it gets eaten
                eat_order = [0, 1]
                random.shuffle(eat_order)
                i_eaten = agents_at_tree[i][eat_order[0]]
                i_survi = agents_at_tree[i][eat_order[1]]

                agent_survi = pop[i_survi]
                agent_eaten = pop[i_eaten]
                if agent_survi.type == T_ALT and \
                        (not ALTRUISTS_ARE_EGOISTS or agent_eaten.type == T_ALT): # if alt egoists, help only other alt
                    new_pop.append(pop[i_eaten])  # originally eaten one survives when altruist yells
                    if np.random.random() > PROB_ALTRUIST_DIES:  # probability that Altruist survives too
                        new_pop.append(pop[i_survi])
                else:  # TODO other type logic
                    new_pop.append(pop[i_survi])

    return new_pop
