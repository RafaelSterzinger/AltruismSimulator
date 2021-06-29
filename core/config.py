import itertools
import time

TIME_STR = time.strftime('%Y-%m-%d-%H-%M-%S')
import numpy as np

NUM_SIMULATIONS = 7  # TODO: averaging in main.py line 91 fails with > 7..

NUM_DAYS = 10000
NUM_POP = 100
PROB_BIRTH = [0.998, 0.001, 0.001]

NUM_TREES = 140
TREES = np.repeat(range(0, NUM_TREES), 2).tolist()
PROB_OF_PREDATOR = 0.003
PROB_ALTRUIST_DIES = 0.5

T_COW = 0  # coward
T_SUC = 1  # sucker
T_GRE = 2  # greenbeard
T_IMP = 3  # impostor
POP_TYPES = {0: 0.25,
             1: 0.25,
             2: 0.25,
             3: 0.25}
TOTAL_TYPE = -1
POP_COLORS = {0: 'blue',
              1: 'yellow',  # TODO: maybe not yellow as single run lines cannot be made out
              2: 'green',
              3: 'red',
              TOTAL_TYPE: 'black'}

# Variables that change at runtime
NUM_PASSED_NIGHTS = 0
ID_COUNTER = itertools.count()

# TODO move to seperate experiment yaml/config file (not config.py)
PLOT_RELATIVE = True  # 3, 4
GREEN_BEARD = False  # 5
POPULATION_SIMULATION = False  # 1
PLOT_TOTAL = False
PLOT_SINGLE_RUNS = True
