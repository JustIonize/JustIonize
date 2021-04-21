from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes
   
xExpt, yExpt = np.loadtxt('phiSpectrum.txt', unpack=True)
#plt.hist(xExpt, weights=yExpt, bins=len(xExpt))
#plt.show()
   
   
   
m_K = 0.493   
nChan = 120
 
nPar = 5
dx = xExpt[1] - xExpt[0]   
   
   
   
def func(x, par):
    
    A = par[0]
    m_phi = par[1]
    g0 = par[2]
    
    p0 = np.sqrt(np.square(m_phi/2) - np.square(m_K))
    p = np.sqrt(np.square(x/2) - np.square(m_K)) 
    g_phi = (m_phi/x) * g0 * np.power(p/p0, 3)
    BW = A*(x*m_phi*g_phi)/(np.square(np.square(x) - np.square(m_phi)) + np.square(m_phi*g_phi))
 
    alpha = par[3]
    beta = par[4]
    BG = alpha*np.power(x - 2*m_K, beta) if x >= 2*m_K else 0
 
    return BW + BG
 
#actPar = [5000, 20., 90., -0.2, 60.]
#rnd = ROOT.TRandom3()

# Area, g, x0, a_bg, b_bg = 5000, 20., 90., -0.2, 60.
#indPos = yExpt > 0
#nPos = indPos.sum()
# CHI-SQUARED\n",

def FCN(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([func(i, par) for i in xExpt]) 
    indPos = yExpt > 0
    arrayFCN = np.square(yExpt[indPos] - yTheor[indPos])/yExpt[indPos]
    valFCN = np.sum(arrayFCN)
    f.value = valFCN
   
# BINNED MAXIMUM LIKELIHOOD
def FCN2(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([func(i, par) for i in xExpt])
    indPos = yExpt > 0
    fi = yTheor[indPos]
    di = yExpt[indPos]
    fi = np.where(fi < 0, 1, fi)
#     arrayFCN = fi - di * np.log(fi)
    arrayFCN = (fi - di) - di * np.log(fi/di)
    valFCN = np.sum(arrayFCN)
    f.value = valFCN
   
   
minuit = ROOT.TMinuit(5)
minuit.SetPrintLevel(1)
minuit.SetFCN(FCN)
errordef = 1.

minuit.DefineParameter(0, 'Area', 1e3, 1e-2, 0., 0.)
minuit.DefineParameter(1, 'm_phi', 1., 1e-4, 0., 0.)
minuit.DefineParameter(2, 'g0', 1, 1e-4, 0., 0.)
minuit.DefineParameter(3, 'a_bg', 0.1, 1e-4, 0., 0.)
minuit.DefineParameter(4, 'b_bg', 2, 1e-4, 0., 0.)

ierflg = ctypes.c_int(0)
minuit.mncomd("SET ERR " + str(1), ierflg)
minuit.mncomd("SET STR 1", ierflg)
minuit.mncomd("MIGRAD 10000 1e-8", ierflg)
 
ndf = nChan - minuit.GetNumFreePars()
print("Chi/ndf = ", valFCN/ndf)
 
valPar = ctypes.c_double(0)
errPar = ctypes.c_double(0)
 
parFit = np.zeros(5)
parErr = np.zeros(5)
 
for i in range(nPar):
    minuit.GetParameter(i, valPar, errPar)
    parFit[i] = valPar.value
    parErr[i] = errPar.value
    
    
xx = np.linspace(0, 1.2, 10000)
yy = [func(i, parFit) for i in xx]
#yy3 = [func(i, parFit2) for i in xx]
 
plt.figure(figsize=(14,10))
 
# plt.plot(xExpt, yExpt, '.', color='black', label='Data')
plt.errorbar(xExpt, yExpt, np.sqrt(yExpt), fmt='.', color='black', capsize=2)
plt.plot(xx, yy, color='r', lw=3, label=r'Fit ($\chi^2$) $\chi^2/ndf = 1.981$')
#plt.plot(xx, yy3, '-.' ,color='g', lw=2, label=r'Fit (BML) $\\chi^2/ndf = 0.964$')

plt.legend(fontsize=15)
 
plt.show()
  
    
