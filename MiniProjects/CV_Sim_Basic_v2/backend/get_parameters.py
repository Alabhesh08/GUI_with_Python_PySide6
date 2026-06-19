def get_parameters():
    HR = 60  # bpm

    T = {
        "cyc": 60 / HR,
        "sys": 0.3,
    }

    T["ee"] = (2 / 3) * T["sys"]
    T["cyc_start"] = 0

    # Compliance
    C = {
        "a": 1.6,
        "v": 100,
        "pa": 4.3,
        "pv": 8.4,
        "dias_l": 10,
        "dias_r": 20,
        "sys_l": 0.4,
        "sys_r": 1.2,
    }

    # Resistances
    R = {
        "a": 1,
        "ri": 0.05,
        "p": 0.08,
        "li": 0.01,
        "lo": 0.01,
        "ro": 0.003,
    }

    # Intrathoracic pressure parameters
    pit_a = -6
    pit_b = -3
    breath_duration = 5
    insp_exp_ratio = 0.5

    # Baroreflex parameters
    B = {
        "switch": 0,
        "gain_para": 0.018,
        "gain_symp_HR": 0.018,
        "gain_symp_Clsys": 0.007,
        "gain_symp_Crsys": 0.021,
        "gain_symp_Ra": 0.011,
        "gain_symp_Vv": 26.5,
    }

    # Unstressed volumes
    V0 = {
        "l": 15,
        "a": 715,
        "v": 2500,
        "r": 15,
        "pa": 90,
        "pv": 490,
    }

    return (
        T,
        C,
        V0,
        R,
        B,
        pit_a,
        pit_b,
        breath_duration,
        insp_exp_ratio,
    )