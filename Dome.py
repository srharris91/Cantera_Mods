def Dome(a,y1='v',y2='P'):
    """Return the values of y1 and y2 of the cantera object at the liquid-vapor dome
    a  -- a cantera module object
    y1 -- an attribute of the cantera module object a (in a string '') (default='v')
    y2 -- an attribute of the cantera module object a (in a string '') (default='P')
    
    """

    # error if attribute not found
    if (hasattr(a,y1)==0):
        raise ValueError("could not find %s attribute of %s" % (y1,a))
    if (hasattr(a,y2)==0):
        raise ValueError("could not find %s attribute of %s" % (y2,a))

    # over the range of pressure values (up to critical point)
    #P=np.linspace(10000,0.99*a.critical_pressure,1000)
    lower=10000.
    upper=0.99 * a.critical_pressure
    length=1000
    P = [lower + x*(upper-lower)/length for x in range(length)]
    X=0 # liquid side
    y1_range=[]
    y2_range=[]
    for p in P:
        a.PX=p,X
        y1_range.append(getattr(a,y1))
        y2_range.append(getattr(a,y2))
    X=1 # vapor side
    for p in P[::-1]:
        a.PX=p,X
        y1_range.append(getattr(a,y1))
        y2_range.append(getattr(a,y2))
    return y1_range,y2_range # return both x,y data points in a list
def Plot(ax,a,x,y):
    """Plot the vapor dome on the axis
    ax -- a matplotlib.pyplot axis subplot or equivalent
    a  -- a cantera module object (default=ct.Water())
    x  -- an attribute of the cantera module object a (in a string '') (default='v')
    y  -- an attribute of the cantera module object a (in a string '') (default='P')
    """

    # a is a cantera module object
    # y1 is an attribute of a (in a string '')
    # y2 is also an attribute of a (in a string '')
    y1_range,y2_range=Dome(a,x,y)
    if (x=='v' or y=='v') and (x=='P' or y=='P'):
        ax.loglog(y1_range,y2_range,'k-',linewidth=3)
    else:
        ax.plot(y1_range,y2_range,'k-',linewidth=3)
    ax.set_xlabel(x)
    ax.set_ylabel(y)

def Process(ax,a1,a2,x,y):
    """Plot the process frome state a1 to a2 on the axis
    Plot the process diagram on ax
    still a work in progress
    """

if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.pyplot as plt
    # test Pv
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
