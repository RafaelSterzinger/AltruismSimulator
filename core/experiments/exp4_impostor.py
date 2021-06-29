import sys

import core.config as cfg

cfg.POP_TYPES = {0: 0.25,
                 1: 0.25,
                 2: 0.25,
                 3: 0.25}
cfg.PLOT_RELATIVE = True
cfg.PLOT_TOTAL = False
cfg.GREEN_BEARD = True  # has to be true
cfg.PLOT_SINGLE_RUNS = False

if len(sys.argv) > 2:
    cfg.PLOT_RELATIVE = bool(sys.argv[1])
if len(sys.argv) > 3:
    cfg.PLOT_TOTAL = bool(sys.argv[2])
