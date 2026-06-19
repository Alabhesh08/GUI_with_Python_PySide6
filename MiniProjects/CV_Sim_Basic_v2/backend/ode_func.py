import numpy as np

from backend.c_var_calc import c_var_calc
from backend.pit_calc import pit_calc
from backend.pressure_calc import pressure_calc
from backend.flow_func import flow_func


def ode_func(
    t,
    x,
    T,
    C,
    V0,
    R,
    pit_a,
    pit_b,
    breath_duration,
    insp_exp_ratio,
):
    # Cardiac cycle timing
    if T["cyc_start"] == 0:
        t_cal = t % T["cyc"]
    else:
        t_cal = t - T["cyc_start"]

    # Time-varying ventricular compliances
    C_local = C.copy()
    C_local["l"] = c_var_calc(
        t_cal, T, C["dias_l"], C["sys_l"]
    )
    C_local["r"] = c_var_calc(
        t_cal, T, C["dias_r"], C["sys_r"]
    )

    # Pressures
    pit = pit_calc(
        t,
        pit_a,
        pit_b,
        breath_duration,
        insp_exp_ratio,
    )

    p_vec = pressure_calc(
        x,
        C_local,
        pit,
        V0,
    )

    # Flows
    q_vec = flow_func(p_vec, R)

    q = {
        "li": q_vec[0],
        "lo": q_vec[1],
        "a": q_vec[2],
        "ri": q_vec[3],
        "ro": q_vec[4],
        "p": q_vec[5],
    }

    # Volume derivatives
    xdot = np.zeros(6)

    xdot[0] = q["li"] - q["lo"]
    xdot[1] = q["lo"] - q["a"]
    xdot[2] = q["a"] - q["ri"]
    xdot[3] = q["ri"] - q["ro"]
    xdot[4] = q["ro"] - q["p"]
    xdot[5] = q["p"] - q["li"]

    return xdot