# AltruismSimulator

__Abstract:__  The concept of fitness and its connotation to survival in the evolutionary sense lead to the emergence of deflection and cooperation-based strategies.
        Conducting a variety of experiments, we analyze the notions of altruism and trust, based on varying levels of (mis)information.
        We show that altruism itself affects population size positively in both true (selfless) and fair (reciprocal) cases.
        With the introduction of misinformation the effectiveness of cooperation decreases substantially.
        As such honesty and trust are key components in societal populations as even with small amounts of deception, altruistic behaviour goes extinct in our experiments.

__Reproducing Results:__

To reproduce our results you first need to clone our repository and afterwards install the dependencies.

    pip install -r requirements.txt

Following that, you can run the following script which will place our plots in `report/figures/archive/`.

    bash run_experiments.sh

This will create plots such as the following.

![Tota](report/figures/exp4_impostor_rel-1.png)

To try out other parameters, feel free to change some of the settings in the `core/experiments/` directory. To e.g.
change the amount of impostors in the last experiment change the population types in `core/experiments/exp4_impostor.py` to the following.

    cfg.POP_TYPES = {0: 0.25,
                     1: 0.25,
                     2: 0.49,
                     3: 0.01}

![Tota](report/figures/exp4_impostor_1-1.png)

    
