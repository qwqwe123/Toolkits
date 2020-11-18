from random import betavariate
import numpy as np
from matplotlib import pyplot as plt


def load(Ht,n):
    vc=np.load("npy/Ht{}_{}by{}_vc_frompos.npy".format(Ht,n,n))
    wc=np.load("npy/Ht{}_{}by{}_wc_frompos.npy".format(Ht,n,n))
    nc=np.load("npy/Ht{}_{}by{}_nc_frompos.npy".format(Ht,n,n))

    return vc,wc,nc

if __name__ == "__main__":
    n=16
    Ht=40
    # vmax=1*(10**-7)
    vmax=100

    lx = n
    ly = n
    itot = n
    jtot = n
    vc,wc,nc = load(Ht,n)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    xs = np.linspace(0., lx, itot)
    ys = np.linspace(0., ly, jtot)
    xs, ys = np.meshgrid(xs, ys)
    ax.set_aspect(1.)
    # ax.pcolor(xs, ys, nc, cmap="jet")
    plt.imshow(nc, cmap="jet",vmin=0, vmax=vmax,extent=[0,32,32,0])
    fig.savefig("./result.png")
    plt.colorbar()
    plt.show()
    plt.close()
