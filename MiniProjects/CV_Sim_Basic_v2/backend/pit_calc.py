import numpy as np


def pit_calc(
    t,
    pit_a,
    pit_b,
    breath_duration,
    insp_exp_ratio,
):
    t_calc = t % breath_duration

    T_exp = breath_duration / (1 + insp_exp_ratio)
    T_insp = breath_duration - T_exp

    if 0 <= t_calc < T_insp:
        pit = (
            (pit_a + pit_b) / 2
            + (pit_b - pit_a) / 2
            * np.cos(np.pi * (t_calc / T_insp))
        )
    else:
        pit = (
            (pit_a + pit_b) / 2
            - (pit_b - pit_a) / 2
            * np.cos(np.pi * (t_calc - T_insp) / T_exp)
        )

    return pit