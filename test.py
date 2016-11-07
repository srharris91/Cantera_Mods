import cantera as ct
import matplotlib.pyplot as plt
from Dome import Dome


P,v = Dome(ct.Water(),'P','v')

fig = plt.figure()
ax = plt.subplot(111)
ax.loglog(v,P,'k-')
plt.show()
