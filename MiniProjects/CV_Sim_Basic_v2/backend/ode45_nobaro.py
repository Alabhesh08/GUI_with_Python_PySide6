import numpy as np
from scipy.integrate import solve_ivp

from backend.c_var_calc import c_var_calc
from backend.pit_calc import pit_calc
from backend.pressure_calc import pressure_calc
from backend.flow_func import flow_func


def ode45_nobaro(
    ode_func,
    T,
    C,
    V0,
    R,
    pit_a,
    pit_b,
    breath_duration,
    insp_exp_ratio,
    t_stamp,
    x0,
):
    # ODE solve
    sol = solve_ivp(
        lambda t, x: ode_func(
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
        ),
        (t_stamp[0], t_stamp[-1]),
        x0,
        method="RK45",
        t_eval=t_stamp,
        max_step=t_stamp[1] - t_stamp[0],
    )

    x = sol.y.T

    # -------------------
    # Volumes
    # -------------------

    V = {
        "l": x[:, 0],
        "a": x[:, 1],
        "v": x[:, 2],
        "r": x[:, 3],
        "pa": x[:, 4],
        "pv": x[:, 5],
    }

    # -------------------
    # Time-varying compliances
    # -------------------

    Cl = np.zeros(len(t_stamp))
    Cr = np.zeros(len(t_stamp))

    for i, t in enumerate(t_stamp):
        Cl[i] = c_var_calc(
            t % T["cyc"],
            T,
            C["dias_l"],
            C["sys_l"],
        )

        Cr[i] = c_var_calc(
            t % T["cyc"],
            T,
            C["dias_r"],
            C["sys_r"],
        )

    # -------------------
    # Pressures
    # -------------------

    p_vec = np.zeros_like(x)
    pit = np.zeros(len(t_stamp))

    for i, t in enumerate(t_stamp):

        C_temp = C.copy()
        C_temp["l"] = Cl[i]
        C_temp["r"] = Cr[i]

        pit[i] = pit_calc(
            t,
            pit_a,
            pit_b,
            breath_duration,
            insp_exp_ratio,
        )

        p_vec[i, :] = pressure_calc(
            x[i, :],
            C_temp,
            pit[i],
            V0,
        )

    p = {
        "l": p_vec[:, 0],
        "a": p_vec[:, 1],
        "v": p_vec[:, 2],
        "r": p_vec[:, 3],
        "pa": p_vec[:, 4],
        "pv": p_vec[:, 5],
        "it": pit,
    }

    # -------------------
    # Flows
    # -------------------

    q_vec = np.zeros_like(x)

    for i in range(len(t_stamp)):
        q_vec[i, :] = flow_func(
            p_vec[i, :],
            R,
        )

    q = {
        "li": q_vec[:, 0],
        "lo": q_vec[:, 1],
        "a": q_vec[:, 2],
        "ri": q_vec[:, 3],
        "ro": q_vec[:, 4],
        "pv": q_vec[:, 5],
    }

    return V, p, q