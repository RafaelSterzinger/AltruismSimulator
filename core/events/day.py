import random
import numpy as np

from core.Blob import Blob
from core.config import NUM_TREES, TREES, PROB_OF_PREDATOR, T_GRE, T_COW, T_IMP, T_SUC, PROB_ALTRUIST_DIES,\
    GREEN_BEARD, POPULATION_SIMULATION


def day(pop: [Blob]):
    # resources are limited to 2*140, exceeding agents die randomly
    random.shuffle(pop)
    if len(pop) > 2 * NUM_TREES:
        pop = pop[:2 * NUM_TREES]

    # selecting faulty resources
    predator_occurrence = np.random.random(NUM_TREES) < PROB_OF_PREDATOR
    agents_at_tree = [[] for _ in range(NUM_TREES)]

    # each agent picks one of the 2 available places of each resource
    selected_tree = random.sample(TREES, len(pop))
    for i_agent, i_tree in enumerate(selected_tree):
        agents_at_tree[i_tree].append(i_agent)
    new_pop = []

    for i in range(0, NUM_TREES):
        # if there is no faulty resource, agents at that tree live on
        if not (predator_occurrence[i]):
            new_pop.extend([pop[i_agent] for i_agent in agents_at_tree[i]])
        else:
            # during the simulation of a stable population, both agents die
            if POPULATION_SIMULATION:
                continue
            # if there is only one agent, it dies
            elif len(agents_at_tree[i]) == 2:
                # mechanics for different types, the agent obtaining the faulty resource is randomly selected
                eat_order = [0, 1]
                random.shuffle(eat_order)
                i_eaten = agents_at_tree[i][eat_order[0]]
                i_survi = agents_at_tree[i][eat_order[1]]

                agent_survi = pop[i_survi]
                agent_eaten = pop[i_eaten]
                if agent_survi.type == T_GRE or agent_survi.type == T_SUC:
                    # if only suckers, help everyone or if greenbeards, help only other greenbeards or impostor
                    if (not GREEN_BEARD or agent_survi.type == T_SUC) or (
                            agent_eaten.type == T_GRE or agent_eaten.type == T_IMP):
                        # originally bound-to-die one survives when altruist shares the resource
                        new_pop.append(pop[i_eaten])
                        if np.random.random() > PROB_ALTRUIST_DIES:
                            # probability that the altruist survives too
                            new_pop.append(pop[i_survi])
                    else:
                        # greenbeard did not share resource with seemingly non-altruistic agent
                        new_pop.append(pop[i_survi])
                elif agent_survi.type == T_COW or agent_survi.type == T_IMP:
                    # if cowards or impostors, altruistic agent dies, the other one survives
                    new_pop.append(pop[i_survi])
    return new_pop
