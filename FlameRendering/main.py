import matplotlib.pyplot as plt

from Animation import Animation
from Plotting import Plotting

path = r'/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/2D/Hele-Shaw/l=200mm,w=5.5mm/ClPhi=1.0Xi=0.5'
# Plot = Plotting(path, 2, (40, 100))
# time_name = '0.1'
# ax = Plot.plot_field_in_time_moment(time_name, 'H2O')
# plt.show()

Anime = Animation(path, 2, (110, 4000), figsize=(16, 1))
Anime.make_amine('T')
