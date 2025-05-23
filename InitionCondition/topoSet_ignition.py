import numpy as np
import matplotlib.pyplot as plt
import random


def split_segment(L, N, Mmin, Mmax):
    # Check if it's possible to split the segment with given constraints
    if N * Mmin > L or N * Mmax < L:
        raise ValueError("Cannot split the segment with the given constraints.")

    segments = []
    remaining_length = L

    for _ in range(N - 1):
        # Generate a random length for the current segment within the allowed range
        segment_length = random.randint(Mmin, min(Mmax, remaining_length - (N - len(segments) - 1) * Mmin))
        segments.append(segment_length)
        remaining_length -= segment_length

    # The last segment takes the remaining length
    segments.append(remaining_length)

    return np.cumsum(np.array(segments))


delta = 0.125e-3
Nx = 620
Ny = 400
Nz = 38
rmin = 0.0008
rmax = 0.0012

n_min = 7
n_max = 18
num_of_cell = int(2 * Ny / n_max) + 1

ss = split_segment(Ny, num_of_cell, n_min + 1, n_max)

p1 = (np.concatenate((np.array([0]), ss[:-1])) + (n_min // 2)) * delta
p2 = (ss - (n_min // 2)) * delta

P = np.array([p1, p2]).T



topoSetDict_file = open("topoSetDict", "w+")
with open('topoSetDict.orig_1', 'r') as orig_1:
    data = orig_1.read()
    topoSetDict_file.write(data)

topoSetDict_file.write("    {\n" +
                       "    name    ignition;\n" +
                       "    type    cellSet;\n" +
                       "    action  new;\n" +
                       "    source  cylinderToCell;\n")
topoSetDict_file.write(f"       p1      ({Nx * delta} {P[0][0]}  {Nz * delta / 2});\n")
topoSetDict_file.write(f"       p2      ({Nx * delta} {P[0][1]}  {Nz * delta / 2});\n")
r = round(np.random.uniform(rmin, rmax), 4)
plt.plot([p1[0], p2[0]], [0, 0], c="red", lw=r*10000)

topoSetDict_file.write(f"       radius  {r};\n")
topoSetDict_file.write("    }\n")

for i in range(1, len(p1)):
    topoSetDict_file.write("    {\n")
    topoSetDict_file.write(f"       name    tmp_{i};\n")
    topoSetDict_file.write("        type    cellZoneSet;\n" +
                           "        action  new;\n" +
                           "        source  cylinderToCell;\n")

    topoSetDict_file.write(f"       p1      ({Nx * delta} {P[i][0]}  {Nz * delta / 2});\n")
    topoSetDict_file.write(f"       p2      ({Nx * delta} {P[i][1]}  {Nz * delta / 2});\n")
    r = round(np.random.uniform(rmin, rmax), 4)
    plt.plot([p1[i], p2[i]], [0, 0], c="red", lw=r*10000)

    topoSetDict_file.write(f"       radius  {r};\n")
    topoSetDict_file.write("    }\n")

    topoSetDict_file.write("    {\n")
    topoSetDict_file.write(f"       name    ignition;\n")
    topoSetDict_file.write("        type    cellSet;\n" +
                           "        action  add;\n" +
                           "        source  zoneToCell;\n")
    topoSetDict_file.write(f"       zone tmp_{i};\n")
    topoSetDict_file.write("    }\n")


with open('topoSetDict.orig_2', 'r') as orig_2:
    data = orig_2.read()
    topoSetDict_file.write(data)

topoSetDict_file.close()
orig_1.close()
orig_2.close()


plt.show()