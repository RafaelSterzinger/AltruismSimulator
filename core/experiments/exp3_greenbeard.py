import sys

import core.config as cfg

cfg.POP_TYPES = {0: 0.5,
                 2: 0.5}
cfg.PLOT_RELATIVE = False
cfg.PLOT_TOTAL = False
cfg.GREEN_BEARD = True

if len(sys.argv) > 2:
    cfg.PLOT_RELATIVE = bool(sys.argv[1])
if len(sys.argv) > 3:
    cfg.PLOT_TOTAL = bool(sys.argv[2])