from pathlib import Path

import numpy as np
from scipy.io import loadmat

from backend.get_parameters import get_parameters
from backend.ode_func import ode_func
from backend.ode45_nobaro import ode45_nobaro
from backend.ode45_withbaro import ode45_withbaro


class CardiovascularSimulator:

    def __init__(
        self,
        v_init_file="V_init.mat",
        use_baroreflex=False,
        simulation_time=120.0,
        dt=0.001,
    ):

        backend_dir = Path(__file__).resolve().parent

        if v_init_file == "V_init.mat":
            self.v_init_file = backend_dir / "V_init.mat"
        else:
            self.v_init_file = Path(v_init_file)
            
        self.use_baroreflex = use_baroreflex
        self.simulation_time = simulation_time
        self.dt = dt

        self.V = None
        self.p = None
        self.q = None
        self.t_stamp = None

    def load_v_init(self):

        mat = loadmat(self.v_init_file)

        V = mat["V"][0, 0]

        return {
            "l": V["l"].flatten(),
            "a": V["a"].flatten(),
            "v": V["v"].flatten(),
            "r": V["r"].flatten(),
            "pa": V["pa"].flatten(),
            "pv": V["pv"].flatten(),
        }

    def run(self):

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

        B["switch"] = int(self.use_baroreflex)

        V_init = self.load_v_init()

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

        self.t_stamp = np.arange(
            0,
            self.simulation_time + self.dt,
            self.dt,
        )

        print(f"Simulation points: {len(self.t_stamp):,}")

        if B["switch"] == 0:

            print("Running without baroreflex...")

            self.V, self.p, self.q = ode45_nobaro(
                ode_func,
                T,
                C,
                V0,
                R,
                pit_a,
                pit_b,
                breath_duration,
                insp_exp_ratio,
                self.t_stamp,
                x0,
            )

        else:

            print("Running with baroreflex...")

            self.V, self.p, self.q = ode45_withbaro(
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
                self.t_stamp,
                x0,
            )

        print("\nSimulation Complete")

        print(
            f"Final LV Volume: "
            f"{self.V['l'][-1]:.2f} mL"
        )

        print(
            f"Final Aortic Pressure: "
            f"{self.p['a'][-1]:.2f} mmHg"
        )

        return (
            self.V,
            self.p,
            self.q,
            self.t_stamp,
        )

    def save_results(
        self,
        filename="python_results.mat",
    ):

        if self.V is None:
            raise RuntimeError(
                "Run simulation before saving."
            )

        from scipy.io import savemat

        savemat(
            filename,
            {
                "V": self.V,
                "p": self.p,
                "q": self.q,
                "t_stamp": self.t_stamp,
            },
        )

        print(f"Results saved to {filename}")