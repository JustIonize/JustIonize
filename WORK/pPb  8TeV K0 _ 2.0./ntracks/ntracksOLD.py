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
xLow01, xTop01, y01, Deltay01 = np.loadtxt('ntracks(2,3).txt', unpack=True)
xLow01Reper, xTop01Reper, y01Reper, Deltay01Reper = np.loadtxt('ntracks(2,3).txt', unpack=True)
y01 = y01/np.amax(y01) #normaized
y01Reper = y01Reper/np.amax(y01Reper) #normaized

Deltay01 = Deltay01/np.amax(y01) #normaized
Deltay01Reper = Deltay01Reper/np.amax(y01Reper) #normaized

yLow01 = y01 - Deltay01/2
yLow01Reper = y01Reper - Deltay01Reper/2

yTop01 = y01 + Deltay01/2
yTop01Reper = y01Reper + Deltay01Reper/2

x01 = ((xLow01+xTop01)/2)
x01Reper = ((xLow01+xTop01)/2)

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
h = ROOT.TH1F('tsallis','Data VS Tsallis', nChan - 1, x01 - dx/2.)
h.SetMarkerColor(ROOT.kBlack)
h. SetLineColor(ROOT.kBlack)
h.SetLineWidth(2)
h.SetMarkerStyle(20)
h.SetMarkerSize(1)
h.GetXaxis().SetTitle('pT [GeV]')
h.GetYaxis().SetTitle('d(sigma)/(dpT dy)')

for chan in range(len(x01)):
    h.SetBinContent(chan + 1,y01[chan])


nChan2 = 50
X = np.linspace(0,5.5,nChan2)
dx = X[1] - X[0]

fFit = ROOT.TH1F('tsallis','Data VS Tsallis', nChan2 - 1, X - dx/2.)
fFit.SetLineColor(ROOT.kRed)
fFit.SetLineWidth(3)
fFit.SetMarkerColor(ROOT.kRed)
fFit.SetMarkerStyle(20)
fFit.SetMarkerSize(1)
fFit.GetXaxis().SetTitle('pT [GeV]')
fFit.GetYaxis().SetTitle('d(sigma)/(dpT dN)')


Y = np.array([Tsallis(i, parFit) for i in X])


for chan in range(nChan2):
    fFit.SetBinContent(chan + 1 ,Y[chan])

Legend = ROOT.TLegend(0.70,0.70,0.90,0.90)
Legend.AddEntry(h,'Data', ' l ')
Legend.AddEntry(fFit,'Fit' , ' l ' )
Legend.SetFillColor(0)

h.Draw()
fFit.Draw("SAME&l")
Legend.Draw("SAME")
#gPad = ROOT.gPad()
#gPad.SetLogy(1)

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(15)
ROOT.gPad.Update()
