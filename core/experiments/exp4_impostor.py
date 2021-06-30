import sys
import core.config as cfg

cfg.POP_TYPES = {0: 0.25,
                 1: 0.25,
                 2: 0.25,
                 3: 0.25}
cfg.PLOT_RELATIVE = True
cfg.PLOT_TOTAL = False
cfg.GREEN_BEARD = True
cfg.PLOT_SINGLE_RUNS = False

if len(sys.argv) > 2:
    cfg.PLOT_RELATIVE = bool(int(sys.argv[2]))
if len(sys.argv) > 3:
    cfg.PLOT_TOTAL = bool(int(sys.argv[3]))
if len(sys.argv) > 4:
    imp_part = float(sys.argv[5])
    cfg.POP_TYPES[2] = 0.5 - imp_part
    cfg.POP_TYPES[3] = imp_part
