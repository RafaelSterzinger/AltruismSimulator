import time

import numpy as np

NUM_DAYS = 1000
NUM_POP = 100
PROB_BIRTH = [0.998, 0.001, 0.001]

NUM_TREES = 140
PROB_OF_PREDATOR = 0.003
TREES = np.repeat(range(0, NUM_TREES), 2).tolist()

NUM_SIMULATIONS = 20

TIME_STR = time.strftime('%Y-%m-%d-%H-%M-%S')
