import sys , time , ROOT
from ROOT import TMinuit
import numpy as np
from math import *
import ctypes 
from ctypes import *


'''
Some parameters
'''

rnd = ROOT.TRandom3()
nChan = 200
nPar = 3
peakArea, FWHM, peakPos   = 5000., 10., 90.

xExpt = np.linspace(1,nChan,nChan)
dx = xExpt[1] - xExpt[0]
yExpt = np.zeros_like(xExpt)

'''
Lorentz distr
'''
muTot = peakArea/(np.pi*FWHM*(1. + ((xExpt - peakPos)/FWHM)**2)) - 0.2*xExpt + 60.

for chan in range(nChan):
    yExpt[chan] = rnd.Poisson(muTot[chan]) 

indPos = yExpt>0
nPos = indPos.sum()


'''
Set FCN
'''
def FCN(npar, gin, f , par , iflag ):
    global valFCN
    Area, halfOfWidth , pos = par[0], par[1], par[2]
    yTheor = Area/(np.pi*halfOfWidth*(1.+((xExpt-pos)/halfOfWidth)**2))-0.2*xExpt+60.
    indPos = yExpt>0
    arrayFCN = (yTheor[indPos] - yExpt[indPos])**2/yExpt[indPos]
    valFCN = np.sum(arrayFCN)
    f.value = valFCN

'''
MINUIT
'''
minuit = ROOT.TMinuit(nPar)
minuit.SetPrintLevel(1)
minuit.SetFCN(FCN)
errordef = 1.

minuit.DefineParameter(0,'Area', 1.e3, 1.e-2, 0.,0.)
minuit.DefineParameter(1,'halfOfWidth', 5., 1.e-4, 0.,0.)
minuit.DefineParameter(2,'pos', 105., 1.e-4, 0.,0.)

ierflg = ctypes.c_int(0)
minuit.mncomd("SET ERR " + str(1), ierflg)
minuit.mncomd("SET STR 1", ierflg)
minuit.mncomd("MIGRAD 10000 1e-8", ierflg)


'''
Get chi square / NDF
'''
NDF = 200 - minuit.GetNumFreePars()
print("Chi/ndf = ", valFCN/NDF)

'''
Make fit
'''
valPar = ctypes.c_double(0)
errPar = ctypes.c_double(0)

parFit = np.zeros(3)
parErr = np.zeros(3)

for i in range(nPar):
    minuit.GetParameter(i, valPar, errPar)
    parFit[i] = valPar.value
    parErr[i] = errPar.value

Area, halfOfWidth, pos = parFit[0], parFit[1], parFit[2]

'''
HISTOGRAM
'''
ROOT.gStyle.SetOptStat(0)
h = ROOT.TH1F('histLorentz','Lozentz & linear bgr',nChan - 1,xExpt - dx/2.)
h.SetMinimum(0)
h.SetMarkerColor(ROOT.kBlack)
h. SetLineColor(ROOT.kBlack)
h.SetMarkerStyle(20)
h.SetMarkerSize(1)
h.GetXaxis().SetTitle('Channels')
h.GetYaxis().SetTitle('Counts')

'''
Real distribution
'''
f1 = ROOT.TF1("f1","[0]/(3.14*[1]*(1+((x-[2])/[1])**2))-0.2*x+60",xExpt[0],xExpt[-1])
f1.SetParameters(peakArea,FWHM, peakPos)
f1.SetLineColor(ROOT.kRed)
f1.SetLineWidth(3)

'''
Fit distribution
'''
fFit = ROOT.TF1('fFit','[0]/(3.14*[1]*(1+((x-[2])/[1])**2))-0.2*x+60',xExpt[0],xExpt[-1])
fFit. SetLineColor(ROOT.kBlue)
fFit.SetParameters(Area, halfOfWidth,pos)

'''
PLOT & LEGEND
'''
Legend = ROOT.TLegend(0.70,0.70,0.90,0.90)
Legend.AddEntry(h,'Data', 'p')
Legend.AddEntry(f1,'Real' , ' l ' )
Legend.AddEntry(fFit,'Fit' , ' l ' )
Legend.SetFillColor(0)

for chan in range(nChan):
    h.SetBinContent(chan + 1,yExpt[chan])
 
  
h.Draw('e')
f1.Draw('same&l')
fFit .Draw('same&l')
ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

Legend.Draw()
time.sleep(10)
ROOT.gPad.Update()
