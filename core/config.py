import itertools
import time
import numpy as np

TIME_STR = time.strftime('%Y-%m-%d-%H-%M-%S')

NUM_SIMULATIONS = 20
PERCENTAGE_TO_PLOT = 0.5

NUM_DAYS = 10000
NUM_POP = 100
PROB_BIRTH = [0.998, 0.001, 0.001]

NUM_RESOURCES = 140
RESOURCES = np.repeat(range(0, NUM_RESOURCES), 2).tolist()
PROB_OF_FAULTY = 0.003
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
              1: 'yellow',
              2: 'green',
              3: 'red',
              TOTAL_TYPE: 'black'}

# variables that change at runtime
NUM_PASSED_NIGHTS = 0
ID_COUNTER = itertools.count()

PLOT_RELATIVE = True
GREEN_BEARD = False
POPULATION_SIMULATION = False
PLOT_TOTAL = False
PLOT_SINGLE_RUNS = True
