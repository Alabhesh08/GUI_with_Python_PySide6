import numpy as np


def ecg():

    N = 1000
    fs = 250

    t = np.arange(N) / fs

    signal = np.zeros_like(t)

    for beat_time in np.arange(0, t[-1], 1.0):

        # P wave
        signal += 0.1 * np.exp(
            -((t - (beat_time + 0.20)) / 0.04) ** 2
        )

        # Q wave
        signal += -0.15 * np.exp(
            -((t - (beat_time + 0.38)) / 0.01) ** 2
        )

        # R wave
        signal += 1.2 * np.exp(
            -((t - (beat_time + 0.40)) / 0.008) ** 2
        )

        # S wave
        signal += -0.25 * np.exp(
            -((t - (beat_time + 0.43)) / 0.012) ** 2
        )

        # T wave
        signal += 0.35 * np.exp(
            -((t - (beat_time + 0.65)) / 0.08) ** 2
        )

    # Baseline wander
    signal += 0.03 * np.sin(
        2 * np.pi * 0.3 * t
    )

    return signal