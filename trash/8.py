"""
================
Lorenz Attractor
================
"""
import numpy as np
import matplotlib.pyplot as plt


R = 0.01
L_0 = 1
L_i = 0.0005

rho_0 = 1.18
T_0 = 300
R_gas = 8.3146 / 0.029
delta_H = 55e6
Y_CH4 = 0.05

kappa = 0.0267
nu = 0.0015
u_n = 0.4
C_v = (5/2) * R_gas * (rho_0 * L_i * np.pi * (R**2) / 0.029)

# A = 8 * np.pi * kappa * (L_0 ** 2) / (C_v * u_n * R)
# B = rho_0 * L_0 * Y_CH4 * delta_H / (C_v * T_0)
C = (2 / 5) # np.pi * (R ** 2) * rho_0 * R_gas * L_0 / C_v
D = L_i * R_gas * T_0 / (L_0 * (u_n ** 2))
E = 4 * nu * L_i / (np.pi  * rho_0 * L_0 * u_n * (R ** 4))

print(D, E)

def lorenz(x, y, z):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = - C * (x * z / y)
    y_dot = z
    z_dot = D * ((x/y) - 1)
    return x_dot, y_dot, z_dot

dt = 0.0005
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (7, 1., 0.)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
plt.plot(dt * np.arange(0, num_steps + 1) * (L_0 / u_n), xs * T_0)
plt.show()

plt.plot(dt * np.arange(0, num_steps + 1) * (L_0 / u_n), ys * L_i)
plt.show()

plt.plot(dt * np.arange(0, num_steps + 1) * (L_0 / u_n), zs * u_n)
plt.show()