import ROOT
from ROOT import TMinuit
import numpy as np
import sys, time
import matplotlib.pyplot as plt
import ctypes

xExp, yExp = np.loadtxt('phiSpectrum.txt', unpack=True)




mk = 0.493 #K+- meson mass in GeV
nChan = 120
nPar = 5
dx = xExp[1] - xExp[0]




def func(x, par):

    #mf, G0, Area, alfa, betta = par[0], par[1], par[2], par[3], par[4]
    Area= par[0]    
    mf= par[1]
    G0= par[2]
    alfa= par[3]
    betta= par[4]
    
    p0 = np.sqrt(np.square(mf/2) - np.square(mk)) 
    p = np.sqrt(np.square(x/2) - np.square(mk)) 
    Gf = (mf/x)*G0*np.power( p/p0,3)
    bw = Area*x*mf*Gf/( np.square(np.square(x)-np.square(mf)) + np.square(mf*Gf)) 
    	
    bgr = alfa*np.power(x - 2*mk,betta) if x >= 2*mk else 0
    	
    return bw + bgr


    
    
def FCN(npar, gin, f , par , iflag ):
    global valFCN
    yTheor = np.array([func(i, par) for i in xExp]) 
    indPos = yExp > 0
    arrayFCN = np.square(yExp[indPos] - yTheor[indPos])/yExp[indPos]
    valFCN = np.sum(arrayFCN)
    f.value = valFCN
    



minuit = ROOT.TMinuit(5)
minuit.SetPrintLevel(1)
minuit.SetFCN(FCN)
errordef = 1.

minuit.DefineParameter(0,'Area', 1.e3, 1.e-2, 0.,0.)
minuit.DefineParameter(1,'mf', 1., 1.e-4, 0.,0.)
minuit.DefineParameter(2,'G0', 1, 1.e-4, 0.,0.)
minuit.DefineParameter(3,'alfa', 0.1, 1.e-4, 0.,0.)
minuit.DefineParameter(4,'betta', 2, 1.e-4, 0.,0.)

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

#mf, G0, Area, alfa , betta  = parFit[0], parFit[1], parFit[2], parFit[3], parFit[4]

'''

xx = np.linspace(0, 1.2, 10000)
yy = [func(i, parFit) for i in xx]
#yy3 = [func(i, parFit2) for i in xx]
 
plt.figure(figsize=(14,10))
 
# plt.plot(xExpt, yExpt, '.', color='black', label='Data')
plt.errorbar(xExp, yExp, np.sqrt(yExp), fmt='.', color='black', capsize=2)
plt.plot(xx, yy, color='r', lw=3, label=r'Fit ($\chi^2$) $\chi^2/ndf = 1.981$')
#plt.plot(xx, yy3, '-.' ,color='g', lw=2, label=r'Fit (BML) $\\chi^2/ndf = 0.964$')

plt.legend(fontsize=15)
 
plt.show()


'''




ROOT.gStyle.SetOptStat(0)
h = ROOT.TH1F('histLorentz','Lozentz & linear bgr', nChan - 1,xExp - dx/2.)
h.SetMarkerColor(ROOT.kBlack)
h. SetLineColor(ROOT.kBlack)
h.SetMarkerStyle(20)
h.SetMarkerSize(1)
h.GetXaxis().SetTitle('Channels')
h.GetYaxis().SetTitle('Counts')

for chan in range(len(xExp)):
    h.SetBinContent(chan + 1,yExp[chan])
    

Y = np.array([func(i, parFit) for i in xExp])

fFit = ROOT.TF1('fFit', Y ,xExp[0],xExp[-1])
fFit. SetLineColor(ROOT.kBlue)


Legend = ROOT.TLegend(0.70,0.70,0.90,0.90)
Legend.AddEntry(h,'Data', 'p')
Legend.AddEntry(fFit,'Fit' , ' l ' )
Legend.SetFillColor(0)


h.Draw()
fFit .Draw('same&l')
ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

Legend.Draw()
time.sleep(10)
ROOT.gPad.Update()

