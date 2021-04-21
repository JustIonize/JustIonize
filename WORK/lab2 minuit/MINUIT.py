import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes
   
x, y = np.loadtxt('phiSpectrum.txt', unpack=True)
dx = x[1] - x[0]    
mk = 0.493
nChan = len(x)
nPar = 5
  

def BWandBGR(m, par):
    #mf, G0, Area, alfa, betta = par[0], par[1], par[2], par[3], par[4]
    Area, mf, G0,alfa, betta = par[0], par[1], par[2], par[3], par[4]
    
    p0 = np.sqrt((mf/2)**2 - (mk)**2)
    p = np.sqrt((m/2)**2 - (mk)**2) 
    g_phi = (mf/m) * G0 * pow(p/p0, 3)
    bw = Area*(m*mf*g_phi)/(((m)**2 - (mf)**2)**2 + (mf*g_phi)**2)

    bgr = 0
    if m >= 2*mk:
        bgr = alfa*np.power(m - 2*mk, betta) 
    else:
        bgr = 0
    total = bw + bgr
    return total
 
'''
FCN for chi
'''
def FCNchi(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([BWandBGR(i, par) for i in x]) 
    indPos = y > 0
    arrayFCN = (y[indPos] - yTheor[indPos])**2/y[indPos]
    valFCN = np.sum(arrayFCN)
    f.value = valFCN
   
'''
FCN for BML
'''
def FCNbml(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([BWandBGR(i, par) for i in x])
    indPos = y > 0
    arrayFCN = ((y[indPos]**2) - y[indPos]*yTheor[indPos])/y[indPos] + yTheor[indPos]*np.log(1 + (yTheor[indPos] - y[indPos])/y[indPos]) 
    valFCN = np.sum(arrayFCN)
    f.value = valFCN


minuit = ROOT.TMinuit(5)
minuit.SetPrintLevel(1)

'''
Chose FCN
'''
#minuit.SetFCN(FCNchi)
minuit.SetFCN(FCNbml)

errordef = 1.


# Chi square start parameters
'''
minuit.DefineParameter(0, 'Area', 1e3, 1e-2, 0., 0.)
minuit.DefineParameter(1, 'mf', 1., 1e-4, 0., 0.)
minuit.DefineParameter(2, 'G0', 1, 1e-4, 0., 0.)
minuit.DefineParameter(3, 'alfa', 0.1, 1e-4, 0., 0.)
minuit.DefineParameter(4, 'betta', 2, 1e-4, 0., 0.)
'''

# BML square start parameters

minuit.DefineParameter(0,'Area', 1.e1, 1.e-2, 0.,0.)
minuit.DefineParameter(1,'mf', 1., 1.e-4, 0.,0.)
minuit.DefineParameter(2,'G0', 0.5, 1.e-4, 0.,0.)
minuit.DefineParameter(3,'alfa', 10, 1.e-4, 0.,0.)
minuit.DefineParameter(4,'betta', 0.2, 1.e-4, 0.,0.)




ierflg = ctypes.c_int(0)
minuit.mncomd("SET ERR " + str(1), ierflg)
minuit.mncomd("SET STR 1", ierflg)
minuit.mncomd("MIGRAD 10000 1e-8", ierflg)
 
NDF = nChan - minuit.GetNumFreePars()
print("Chi/NDF = ", valFCN/NDF)
 
valPar = ctypes.c_double(0)
errPar = ctypes.c_double(0)
 
parFit = np.zeros(5)
parErr = np.zeros(5)
 
for i in range(nPar):
    minuit.GetParameter(i, valPar, errPar)
    parFit[i] = valPar.value
    parErr[i] = errPar.value
    
    
'''
PLOT
'''    
ROOT.gStyle.SetOptStat(0)
h = ROOT.TH1F('histBW','BW & BGR', nChan - 1,x - dx/2.)
h.SetMarkerColor(ROOT.kBlack)
h. SetLineColor(ROOT.kBlack)
h.SetLineWidth(2)
h.SetMarkerStyle(20)
h.SetMarkerSize(1)
h.GetXaxis().SetTitle('Channels')
h.GetYaxis().SetTitle('Counts')

for chan in range(len(x)):
    h.SetBinContent(chan + 1,y[chan])

fFit = ROOT.TH1F('fFit','BW & BGR', nChan - 1,x - dx/2.)
fFit.SetLineColor(ROOT.kRed)
fFit.SetLineWidth(3)
fFit.SetMarkerColor(ROOT.kRed)
fFit.SetMarkerStyle(20)
fFit.SetMarkerSize(1)
fFit.GetXaxis().SetTitle('Channels')
fFit.GetYaxis().SetTitle('Counts')

Y = np.array([BWandBGR(i, parFit) for i in x])
i = 0
while i <= 12:
    Y[i] = 0
    i = i+1

for chan in range(len(x)):
    fFit.SetBinContent(chan + 1 ,Y[chan])

Legend = ROOT.TLegend(0.70,0.70,0.90,0.90)
Legend.AddEntry(h,'Data', ' l ')
Legend.AddEntry(fFit,'Fit' , ' l ' )
Legend.SetFillColor(0)

fFit.Draw()
h.Draw("SAME")
Legend.Draw("SAME")
ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(10)
ROOT.gPad.Update()   
