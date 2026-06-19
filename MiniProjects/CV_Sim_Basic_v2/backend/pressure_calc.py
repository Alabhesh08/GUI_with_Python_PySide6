import numpy as np


def pressure_calc(x, C, pit, V0):
    p = np.zeros(6)

    V = {
        "l": x[0],
        "a": x[1],
        "v": x[2],
        "r": x[3],
        "pa": x[4],
        "pv": x[5],
    }

    p[0] = (V["l"] - V0["l"]) / C["l"] + pit
    p[1] = (V["a"] - V0["a"]) / C["a"]
    p[2] = (V["v"] - V0["v"]) / C["v"]
    p[3] = (V["r"] - V0["r"]) / C["r"] + pit
    p[4] = (V["pa"] - V0["pa"]) / C["pa"]
    p[5] = (V["pv"] - V0["pv"]) / C["pv"]

    return p