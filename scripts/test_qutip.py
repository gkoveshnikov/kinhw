from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 1.0  # angular frequency
times = np.linspace(0, 10, 100)

# Initial state: ground state
psi0 = basis(2, 0)

# Hamiltonian for two-level system
H = omega * sigmax()

# Time evolution (Schrödinger equation)
result = sesolve(H, psi0, times, [sigmaz(), sigmay()])

# Plot expectation values
plt.plot(times, result.expect[0], label='⟨σz⟩')
plt.plot(times, result.expect[1], label='⟨σy⟩')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Expectation values')
plt.show()

