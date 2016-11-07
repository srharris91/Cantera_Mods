import cantera as ct
import numpy as np

def Dome(a,y1,y2):
    # a is a cantera module object
    # y1 is an attribute of a (in a string '')
    # y2 is also an attribute of a (in a string '')
    if (hasattr(a,y1)==0):
        raise ValueError("could not find %s attribute of %s" % (y1,a))
    if (hasattr(a,y2)==0):
        raise ValueError("could not find %s attribute of %s" % (y2,a))

    P=np.linspace(10000,0.99*a.critical_pressure,1000)
    X=0
    y1_range=[]
    y2_range=[]
    for p in P:
        a.PX=p,X
        y1_range.append(getattr(a,y1))
        y2_range.append(getattr(a,y2))
    X=1
    for p in P[::-1]:
        a.PX=p,X
        y1_range.append(getattr(a,y1))
        y2_range.append(getattr(a,y2))
    return y1_range,y2_range

if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    # test Pv
    P,v = Dome(ct.Water(),'T','h')
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(v,P,'k-')
    plt.show()
    P,v = Dome(ct.Water(),'r','h')
