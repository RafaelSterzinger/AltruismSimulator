import sys

import core.config as cfg

cfg.POP_TYPES = {0: 0.5,
                 1: 0.5}
cfg.PLOT_RELATIVE = False
cfg.PLOT_TOTAL = True

if len(sys.argv) > 1:
    cfg.PLOT_RELATIVE = bool(sys.argv[1])
if len(sys.argv) > 2:
    cfg.PLOT_TOTAL = bool(sys.argv[2])
