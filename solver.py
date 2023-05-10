"""A solver for the 1D Diffusion Equation"""

import numpy as np


np.set_printoptions(formatter={"float": "{: 6.1f}".format})


def solv1d(concentration, spacing, time_step, diffusivity):
    flux = -diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] -= time_step * np.diff(flux) / spacing
    return concentration


def _example():
    dx = 0.5
    C1 = 500
    C2 = 0
    Lx = 10
    D = 100
    
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1
    C[int(Lx/2) :] = C2
    dt = dx * dx / D / 2.1
    
    for _ in range(1, 5):
        C = solv1d(C, dx, dt, D)
        print(C)

    
if __name__ == "__main__":
    _example()
    
    