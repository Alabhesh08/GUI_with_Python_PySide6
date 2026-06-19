import numpy as np
from scipy.io import loadmat

from get_parameters import get_parameters
from ode_func import ode_func
from ode45_nobaro import ode45_nobaro
from ode45_withbaro import ode45_withbaro


def load_v_init(filename="D:\\Labhesh\\IITM\\Programming\\GUI_with_Python_PySide6\\MiniProjects\\CV_Sim_Basic_v2\\backend\\V_init.mat"):
    """
    Load MATLAB struct V from V_init.mat
    """

    mat = loadmat(filename)

    V = mat["V"][0, 0]

    return {
        "l": V["l"].flatten(),
        "a": V["a"].flatten(),
        "v": V["v"].flatten(),
        "r": V["r"].flatten(),
        "pa": V["pa"].flatten(),
        "pv": V["pv"].flatten(),
    }


def main():

    # ==========================================================
    # Parameters
    # ==========================================================

    (
        T,
        C,
        V0,
        R,
        B,
        pit_a,
        pit_b,
        breath_duration,
        insp_exp_ratio,
    ) = get_parameters()

    # 0 = without baroreflex
    # 1 = with baroreflex  # Doesn't give same results in python as matlab, so not using it for now.
    B["switch"] = 0

    # ==========================================================
    # Initial Conditions
    # ==========================================================

    V_init = load_v_init("V_init.mat")

    x0 = np.array(
        [
            V_init["l"][-1],
            V_init["a"][-1],
            V_init["v"][-1],
            V_init["r"][-1],
            V_init["pa"][-1],
            V_init["pv"][-1],
        ],
        dtype=float,
    )

    # ==========================================================
    # Simulation Parameters
    # ==========================================================

    T_end = 120.0
    dt = 0.001

    t_stamp = np.arange(
        0,
        T_end + dt,
        dt,
    )

    print(f"Simulation points: {len(t_stamp):,}")

    # ==========================================================
    # Run Simulation
    # ==========================================================

    if B["switch"] == 0:

        print("Running without baroreflex...")

        V, p, q = ode45_nobaro(
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
        )

    else:

        print("Running with baroreflex...")

        V, p, q = ode45_withbaro(
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
        )

    # ==========================================================
    # Example Outputs
    # ==========================================================

    print("\nSimulation Complete")

    print(f"Final LV Volume: {V['l'][-1]:.2f} mL")
    print(f"Final Aortic Pressure: {p['a'][-1]:.2f} mmHg")

    return V, p, q, t_stamp


if __name__ == "__main__":
    V, p, q, t_stamp = main()


from scipy.io import savemat

savemat(
    "python_results.mat",
    {
        "V": V,
        "p": p,
        "q": q,
        "t_stamp": t_stamp
    }
)