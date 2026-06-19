import numpy as np

def c_var_calc(t_cal, T, C_dias, C_sys):
    """
    Parameters
    ----------
    t_cal : float
    T : object or dict with attributes/keys 'sys' and 'ee'
    C_dias : float
    C_sys : float

    Returns
    -------
    float
        Time-varying capacitance
    """

    E_dias = 1.0 / C_dias
    E_sys = 1.0 / C_sys

    T_sys = T["sys"] if isinstance(T, dict) else T.sys
    T_ee = T["ee"] if isinstance(T, dict) else T.ee

    if t_cal > T_sys:
        C = 1.0 / E_dias
    else:
        if t_cal < T_ee:
            C = 1.0 / (
                E_dias
                + (E_sys - E_dias)
                * np.cos(0.5 * np.pi * t_cal / T_ee - np.pi / 2)
            )
        else:
            C = 1.0 / (
                E_dias
                + (E_sys - E_dias)
                * np.cos(0.5 * np.pi * (t_cal - T_ee) / (0.5 * T_ee))
            )

    return C