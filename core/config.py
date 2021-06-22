import itertools
import time

TIME_STR = time.strftime('%Y-%m-%d-%H-%M-%S')
import numpy as np

NUM_SIMULATIONS = 20

NUM_DAYS = 1000
NUM_POP = 100
PROB_BIRTH = [0.998, 0.001, 0.001]

NUM_TREES = 140
TREES = np.repeat(range(0, NUM_TREES), 2).tolist()
PROB_OF_PREDATOR = 0.003
PROB_ALTRUIST_DIES = 0.5

T_ALT = 0  # altruist
T_COW = 1  # coward
T_SUC = 2  # sucker
T_IMP = 3  # impostor
POP_TYPES = {0: 0.5,
             1: 0.5}

# Variables that change at runtime
NUM_PASSED_NIGHTS = 0
ID_COUNTER = itertools.count()
