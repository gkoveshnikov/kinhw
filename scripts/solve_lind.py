import csv
from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# Parameters
B = 1.0           # magnetic field strength
a = 0.1*0.000001            # dephasing rate
b_plus = 0.2*0.000001       # excitation rate
b_minus = 0.3*0.000001      # relaxation rate

# Pauli matrices and ladder operators
sz = sigmaz()
sp = sigmap()  # σ+
sm = sigmam()  # σ-

# Hamiltonian: H = B * σz
H = B * sz

# Collapse operators
c_ops = [
    a * sz,         # dephasing
    b_plus * sp,    # excitation
    b_minus * sm    # relaxation
]

# Initial state
psi = (basis(2, 0) + basis(2, 1)).unit()  # normalized superposition
rho0 = psi * psi.dag()
#rho0 = basis(2, 0) * basis(2, 0).dag()

# Time grid
tlist = np.linspace(0, 10, 200)

# Solve master equation
result = mesolve(H, rho0, tlist, c_ops, [sigmax(), sigmay(), sigmaz()])

# Plot expectation values
plt.plot(tlist, result.expect[0], label="⟨σx⟩")
plt.plot(tlist, result.expect[1], label="⟨σy⟩")
plt.plot(tlist, result.expect[2], label="⟨σz⟩")
plt.xlabel('Time')
plt.ylabel('Expectation values')
plt.legend()
plt.title('Qubit Evolution with Lindblad Dissipation')
plt.grid()
plt.show()
# Save to CSV
with open("qubit_evolution.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["# t", "nx", "ny", "nz"])
    for i, t in enumerate(tlist):
        nx = result.expect[0][i]
        ny = result.expect[1][i]
        nz = result.expect[2][i]
        writer.writerow([t, nx, ny, nz])

print("CSV file 'qubit_evolution.csv' saved.")
