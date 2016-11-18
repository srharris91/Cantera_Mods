import cantera as ct
import matplotlib.pyplot as plt
import Dome as Dome
# create figure and subplots
fig = plt.figure()
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)
# plot using Dome command
P,v = Dome.Dome(ct.Water(),'P','v')
ax1.loglog(v,P,'k-')
# add plot using Plot command
Dome.Plot(ax2,ct.Water(),'v','P')
# add second plot using Plot command
Dome.Plot(ax3,ct.Water(),'s','T')
# display figure
plt.show()
