import numpy as np

def flow_func(x, R):
    """
    Parameters
    ----------
    x : array-like
        [l, a, v, r, pa, pv]
    R : dict
        Resistance parameters

    Returns
    -------
    np.ndarray
        Flow vector q
    """

    q = np.zeros(len(x))

    p = {
        "l": x[0],
        "a": x[1],
        "v": x[2],
        "r": x[3],
        "pa": x[4],
        "pv": x[5]
    }

    # Mitral valve
    if p["pv"] > p["l"]:
        q[0] = (p["pv"] - p["l"]) / R["li"]
    else:
        q[0] = 0

    # Aortic valve
    if p["l"] > p["a"]:
        q[1] = (p["l"] - p["a"]) / R["lo"]
    else:
        q[1] = 0

    # Systemic circulation
    q[2] = (p["a"] - p["v"]) / R["a"]

    # Tricuspid valve
    if p["v"] > p["r"]:
        q[3] = (p["v"] - p["r"]) / R["ri"]
    else:
        q[3] = 0

    # Pulmonary valve
    if p["r"] > p["pa"]:
        q[4] = (p["r"] - p["pa"]) / R["ro"]
    else:
        q[4] = 0

    # Pulmonary circulation
    q[5] = (p["pa"] - p["pv"]) / R["p"]

    return q