import ROOT
from ROOT import TMinuit
import numpy as np
import matplotlib.pyplot as plt
import ctypes

def cauchy_and_linear_par(x, par):
    return par[0]*((1/np.pi)*par[1]/(np.square(x - par[2]) + np.square(par[1]))) + par[3]*x + par[4]

actPar = [5000, 20., 90., -0.2, 60.]
rnd = ROOT.TRandom3()
nChan = 200
xExpt = np.linspace(1, nChan, nChan)
Tot = [cauchy_and_linear_par(i, actPar) for i in xExpt]
yExpt = np.zeros_like(xExpt)

for chan in range(nChan):
    yExpt[chan] = rnd.Poisson(Tot[chan])
    
nPar = 5
dx = xExpt[1] - xExpt[0]
Area, g, x0, a_bg, b_bg = 5000, 20., 90., -0.2, 60.
indPos = yExpt > 0
nPos = indPos.sum()

    
def FCN(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([cauchy_and_linear_par(i, par) for i in xExpt]) 
    indPos = yExpt > 0
    arrayFCN = np.square(yTheor[indPos]- yExpt[indPos])/yExpt[indPos]
    valFCN = np.sum(arrayFCN)
    f.value = valFCN

minuit = ROOT.TMinuit(5)
minuit.SetPrintLevel(1)
minuit.SetFCN(FCN)
errordef = 1.

minuit.DefineParameter(0, 'Area', 1e3, 1e-2, 0., 0.)
minuit.DefineParameter(1, 'g', 10., 1e-4, 0., 0.)
minuit.DefineParameter(2, 'x0', 100, 1e-4, 0., 0.)
minuit.DefineParameter(3, 'a_bg', -0.3, 1e-4, 0., 0.)
minuit.DefineParameter(4, 'b_bg', 50, 1e-4, 0., 0.)

ierflg = ctypes.c_int(0)
minuit.mncomd("SET ERR " + str(1), ierflg)
minuit.mncomd("SET STR 1", ierflg)
minuit.mncomd("MIGRAD 10000 1e-8", ierflg)

ndf = 200 - minuit.GetNumFreePars()
print("Chi/ndf = ", valFCN/ndf)

valPar = ctypes.c_double(0)
errPar = ctypes.c_double(0)

parFit = np.zeros(5)
parErr = np.zeros(5)

for i in range(nPar):
    minuit.GetParameter(i, valPar, errPar)
    parFit[i] = valPar.value
    parErr[i] = errPar.value

print(parFit)

xx = np.linspace(1, 200, 200)
yy = [cauchy_and_linear_par(i, parFit) for i in xx]
yy2 = [cauchy_and_linear_par(i, actPar) for i in xx]

plt.figure(figsize=(14,10))

plt.plot(xExpt, yExpt, '.', color='black', label='Data')
plt.plot(xx, yy, color='r', lw=3, label='Fit')
plt.plot(xx, yy2, '--' ,color='b', lw=2, label='Actual curve')
plt.legend(fontsize=15)

plt.show()
