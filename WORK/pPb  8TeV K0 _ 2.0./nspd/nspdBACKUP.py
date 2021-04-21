import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes

mk = 0.497648 #GeV
nPar = 3

'''
nspd
'''

data = 'nspd(0,1).txt'
data1 = 'nspd(2,3).txt'
data2 = 'nspd(4,5).txt'
DATA = ['nspd(0,1).txt','nspd(2,3).txt','nspd(4,5).txt']




xLow01, xTop01, y01, Deltay01 = np.loadtxt(data, unpack=True)
xLow01Reper, xTop01Reper, y01Reper, Deltay01Reper = np.loadtxt(data, unpack=True)
x, xTop, y, Deltay = np.loadtxt(data, unpack=True)

y01 = y01/np.amax(y) #normaized
y01Reper = y01Reper/np.amax(y) #normaized

Deltay01 = Deltay01/np.amax(y) #normaized
Deltay01Reper = Deltay01Reper/np.amax(y) #normaized

yLow01 = y01 - Deltay01/2
yLow01Reper = y01Reper - Deltay01Reper/2

yTop01 = y01 + Deltay01/2
yTop01Reper = y01Reper + Deltay01Reper/2

x01 = ((xLow01+xTop01)/2)
x01Reper = ((xLow01+xTop01)/2)

Deltax01 = x01 - xLow01
Deltax01Reper = x01Reper - xLow01Reper

x01.sort()
nChan = len(x01)
dx = 0.01

i = 0
while i <= len(x01)-1:
    j = 0
    while j <= len(x01)-1:
        if x01[i] == x01Reper[j]:
            y01[i] = y01Reper[j]
            Deltay01[i] = Deltay01Reper[j]
            yLow01[i] = yLow01Reper[j]
            yTop01[i] = yTop01Reper[j]
            Deltax01[i] = Deltax01Reper[j]
            j = j + 1
        else:
            j = j + 1
    i = i + 1
'''
Tsallis distr
'''
def Tsallis(pT, par):
    Area, Temper, Q = par[0], par[1], par[2]
    return Area*pT*pow( (1 - (Q-1)*((mk**2 + pT**2)**(0.5) - mk)/Temper) , (1/(Q-1)) )
'''
#FCN for chi
'''
def FCNchi(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([Tsallis(i, par) for i in x01]) 
    indPos = y01 > 0
    arrayFCN = (y01[indPos] - yTheor[indPos])**2/y01[indPos]
    valFCN = np.sum(arrayFCN)
    f.value = valFCN
'''
#FCN for BML
'''
def FCNbml(npar, gin, f, par, iflag):
    global valFCN
    yTheor = np.array([Tsallis(i, par) for i in x01])
    indPos = y01 > 0
    arrayFCN = ((y01[indPos]**2) - y01[indPos]*yTheor[indPos])/y01[indPos] + yTheor[indPos]*np.log(1 + (yTheor[indPos] - y01[indPos])/y01[indPos]) 
    valFCN = np.sum(arrayFCN)
    f.value = valFCN
'''
MIUNIT
'''
minuit = ROOT.TMinuit(5)
minuit.SetPrintLevel(1)
minuit.SetFCN(FCNchi)
#minuit.SetFCN(FCNbml)
errordef = 1.

# Chi square start parameters
minuit.DefineParameter(0, 'Area', 4, 1e-4, 0., 0.)
minuit.DefineParameter(1, 'Temper', 0.1, 1e-4, 0., 0.)
minuit.DefineParameter(2, 'Q', 0.99, 1e-4, 0., 0.)

# BML square start parameters
'''
minuit.DefineParameter(0, 'Area', 1e3, 1e-2, 0., 0.)
minuit.DefineParameter(1, 'Temper', 1., 1e-4, 0., 0.)
minuit.DefineParameter(2, 'Q', 1, 1e-4, 0., 0.)
'''

ierflg = ctypes.c_int(0)
minuit.mncomd("SET ERR " + str(1), ierflg)
minuit.mncomd("SET STR 1", ierflg)
minuit.mncomd("MIGRAD 100000 1e-8", ierflg)
 
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

Err = ROOT.TGraphErrors(nChan - 1, x01, y01, Deltax01, Deltay01)
Err.SetMarkerStyle(20)
Err.SetMarkerColor(1)
Err.SetMarkerSize(1.3)
Err.SetLineWidth(2)
Err.GetXaxis().SetTitle('p_{T} [GeV]')
Err.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Err.SetTitle("LHCb 8 TeV")

nChan2 = 50
X = np.linspace(0,4.0,nChan2)
dx = X[1] - X[0]

fFit = ROOT.TH1F('tsallis','Data VS Tsallis', nChan2 - 1, X - dx/2.)
fFit.SetLineColor(ROOT.kBlack)
fFit.SetLineWidth(3)

Y = np.array([Tsallis(i, parFit) for i in X])
for chan in range(nChan2):
    fFit.SetBinContent(chan + 1 ,Y[chan])

print(X, '\n', Y)

Legend = ROOT.TLegend(0.60,0.70,0.90,0.90)
Legend.AddEntry(Err,'0 < npds < 100', ' p ')
Legend.AddEntry(fFit,'Fit' , ' l ' )
Legend.SetFillColor(0)

Err.Draw("AP")
fFit.Draw("SAME&l")
Legend.Draw("SAME")

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(20)
ROOT.gPad.Update()
