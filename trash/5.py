import matplotlib.pyplot as plt
import numpy as np
import openfoamparser_mai as Ofpp


# setup some generic data
N = 10
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
print(x)
# mask out the negative and positive values, respectively
Zpos = np.ma.masked_less(Z, 0)
Zneg = np.ma.masked_greater(Z, 0)

shp = (70, 4000)

V=Ofpp.parse_internal_field('T')
V = V.reshape(shp)


fig, ax1 = plt.subplots(figsize=(13, 3))

# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = ax1.imshow(V, cmap='Reds', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which Axes object it should be near
fig.colorbar(pos, ax=ax1)

# repeat everything above for the negative data
# # you can specify location, anchor and shrink the colorbar
# neg = ax2.imshow(V, cmap='Reds_r', interpolation='none')
# fig.colorbar(neg, ax=ax2, location='right', anchor=(0, 0.3), shrink=0.7)
#
# # Plot both positive and negative values between +/- 1.2
# pos_neg_clipped = ax3.imshow(V, cmap='RdBu', vmin=-1.2, vmax=1.2,
#                              interpolation='none')
# # Add minorticks on the colorbar to make it easy to read the
# # values off the colorbar.
# cbar = fig.colorbar(pos_neg_clipped, ax=ax3, extend='both')
# cbar.minorticks_on()
plt.show()