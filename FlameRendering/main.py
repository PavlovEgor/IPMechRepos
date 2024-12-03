import matplotlib.pyplot as plt

from Animation import Animation
from Plotting import Plotting

path = r'/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/2D/Hele-Shaw/l=200mm,w=5.0mm/ClPhi=1.0Xi=0.5'
# Plot = Plotting(path, 2, (80, 4000))
# time_name = '0.000100585'
# ax = Plot.plot_field_in_time_moment(time_name, 'H2O')
# plt.show()

Anime = Animation(path, 2, (90, 4000), figsize=(16, 1.5))
Anime.make_amine('H2O')
