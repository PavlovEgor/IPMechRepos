import matplotlib.pyplot as plt

from Animation import Animation
from Plotting import Plotting

path = r'C:\Users\Mi\Documents\PycharmProjects\IPMechRepos\counterFlowFlame2D'
# Plot = Plotting(path, 2, (40, 100))
# time_name = '0.1'
# ax = Plot.plot_field_in_time_moment(time_name, 'H2O')
# plt.show()

Anime = Animation(path, 2, (40, 100))
Anime.make_amine('H2O')
