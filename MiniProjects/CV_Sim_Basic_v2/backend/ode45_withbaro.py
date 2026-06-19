import numpy as np
from scipy.integrate import solve_ivp

from backend.c_var_calc import c_var_calc
from backend.pit_calc import pit_calc
from backend.pressure_calc import pressure_calc
from backend.flow_func import flow_func


def ode45_withbaro(
    ode_func,
    T,
    C,
    V0,
    R,
    B,
    pit_a,
    pit_b,
    breath_duration,
    insp_exp_ratio,
    t_stamp,
    x0,
):
    r = 0.0

    dt = t_stamp[1] - t_stamp[0]
    N_steps = len(t_stamp)

    dt_sym = 0.1
    dt_para = 0.01

    x_out = np.zeros((N_steps, len(x0)))
    p_vec = np.zeros((N_steps, 6))
    q_vec = np.zeros((N_steps, 6))
    pit_vec = np.zeros(N_steps)

    # Initial conditions

    x_out[0, :] = x0

    C_temp = C.copy()
    C_temp["l"] = c_var_calc(
        t_stamp[0],
        T,
        C["dias_l"],
        C["sys_l"],
    )

    C_temp["r"] = c_var_calc(
        t_stamp[0],
        T,
        C["dias_r"],
        C["sys_r"],
    )

    pit_vec[0] = pit_calc(
        t_stamp[0],
        pit_a,
        pit_b,
        breath_duration,
        insp_exp_ratio,
    )

    p_vec[0, :] = pressure_calc(
        x0,
        C_temp,
        pit_vec[0],
        V0,
    )

    q_vec[0, :] = flow_func(
        p_vec[0, :],
        R,
    )

    # Save baseline parameters

    R_base = R.copy()
    C_base = C.copy()
    T_base = T.copy()
    V0_base = V0.copy()

    MAP_setpoint = 100

    control_sym = np.zeros(3)
    control_para = np.zeros(3)

    max_delay_idx_symp = round(30 / dt_sym) + 1
    err_sym_history = np.zeros(max_delay_idx_symp)

    max_delay_idx_para = round(1 / dt_para) + 1
    err_para_history = np.zeros(max_delay_idx_para)

    idx_symp_2s = round(2 / dt_sym)
    idx_symp_5s = round(5 / dt_sym)
    idx_symp_30s = round(30 / dt_sym)

    idx_para_050 = round(0.5 / dt_para)
    idx_para_075 = round(0.75 / dt_para)
    idx_para_100 = round(1.0 / dt_para)

    out_idx = 0

    while out_idx < N_steps - 1:

        t_current = t_stamp[out_idx]

        idx_map_start = max(
            0,
            out_idx - round(dt_para / dt),
        )

        current_MAP = np.mean(
            p_vec[idx_map_start:out_idx + 1, 1]
        )

        # -------------------
        # Sympathetic loop
        # -------------------

        if (
            abs(t_current % dt_sym) < 1e-5
            or t_current == 0
        ):

            err_sym = current_MAP - MAP_setpoint

            err_sym_history[1:] = err_sym_history[:-1]
            err_sym_history[0] = err_sym

            control_sym[0] = (
                2 * control_sym[1]
                - control_sym[2]
                + (dt_sym**2)
                * (1 / (14 * 75))
                * (
                    25 * err_sym_history[idx_symp_2s]
                    - 28 * err_sym_history[idx_symp_5s]
                    + 3 * err_sym_history[idx_symp_30s]
                )
            )

            R["a"] = (
                R_base["a"]
                - B["gain_symp_Ra"] * control_sym[0]
            )

            C["sys_l"] = (
                C_base["sys_l"]
                - B["gain_symp_Clsys"] * control_sym[0]
            )

            C["sys_r"] = (
                C_base["sys_r"]
                - B["gain_symp_Crsys"] * control_sym[0]
            )

            V0["v"] = (
                V0_base["v"]
                + B["gain_symp_Vv"] * control_sym[0]
            )

            control_sym[2] = control_sym[1]
            control_sym[1] = control_sym[0]

        # -------------------
        # Parasympathetic loop
        # -------------------

        err_para = current_MAP - MAP_setpoint

        err_para_history[1:] = err_para_history[:-1]
        err_para_history[0] = err_para

        control_para[0] = (
            2 * control_para[1]
            - control_para[2]
            + 16 * (dt_para**2)
            * (
                err_para_history[idx_para_050]
                - 2 * err_para_history[idx_para_075]
                + err_para_history[idx_para_100]
            )
        )

        control_para[2] = control_para[1]
        control_para[1] = control_para[0]

        # -------------------
        # Integrate next 10 ms
        # -------------------

        idx_end = min(
            N_steps - 1,
            out_idx + round(dt_para / dt),
        )

        t_window = t_stamp[out_idx:idx_end + 1]

        if len(t_window) > 1:

            curr_x = x_out[out_idx, :]

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
                (t_window[0], t_window[-1]),
                curr_x,
                method="RK45",
                t_eval=t_window,
                max_step=dt,
            )

            x_sol = sol.y.T

            for k in range(1, len(t_window)):

                t_k = t_window[k]
                x_k = x_sol[k]

                C_temp = C.copy()

                C_temp["l"] = c_var_calc(
                    t_k - T["cyc_start"],
                    T,
                    C["dias_l"],
                    C["sys_l"],
                )

                C_temp["r"] = c_var_calc(
                    t_k - T["cyc_start"],
                    T,
                    C["dias_r"],
                    C["sys_r"],
                )

                pit_k = pit_calc(
                    t_k,
                    pit_a,
                    pit_b,
                    breath_duration,
                    insp_exp_ratio,
                )

                p_k = pressure_calc(
                    x_k,
                    C_temp,
                    pit_k,
                    V0,
                )

                q_k = flow_func(
                    p_k,
                    R,
                )

                gidx = out_idx + k

                x_out[gidx, :] = x_k
                p_vec[gidx, :] = p_k
                q_vec[gidx, :] = q_k
                pit_vec[gidx] = pit_k

            out_idx = idx_end

        # -------------------
        # IPFM heart rate model
        # -------------------

        delta_T_RRI = (
            B["gain_para"] * control_para[0]
            + B["gain_symp_HR"] * control_sym[0]
        )

        m = 1 / max(
            0.1,
            T_base["cyc"] + delta_T_RRI,
        )

        r += m * dt_para

        if r >= 1:
            r = 0

            T["cyc"] = (
                t_stamp[out_idx]
                - T["cyc_start"]
            )

            T["cyc_start"] = t_stamp[out_idx]

    V = {
        "l": x_out[:, 0],
        "a": x_out[:, 1],
        "v": x_out[:, 2],
        "r": x_out[:, 3],
        "pa": x_out[:, 4],
        "pv": x_out[:, 5],
    }

    p = {
        "l": p_vec[:, 0],
        "a": p_vec[:, 1],
        "v": p_vec[:, 2],
        "r": p_vec[:, 3],
        "pa": p_vec[:, 4],
        "pv": p_vec[:, 5],
        "it": pit_vec,
    }

    q = {
        "li": q_vec[:, 0],
        "lo": q_vec[:, 1],
        "a": q_vec[:, 2],
        "ri": q_vec[:, 3],
        "ro": q_vec[:, 4],
        "pv": q_vec[:, 5],
    }

    return V, p, q