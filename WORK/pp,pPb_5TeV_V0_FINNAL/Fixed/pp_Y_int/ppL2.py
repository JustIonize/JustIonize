import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
from ROOT import TCanvas, TGraph, TPaveLabel, TLatex
from ROOT import gROOT
import matplotlib.pyplot as plt
import ctypes


DATA = 'ppL2Yint.txt'
X, DeltaX, Y1, DeltaY1 = np.loadtxt(DATA, unpack=True)
nChan = len(X)

x = np.array(X)
ex = np.array(DeltaX)
y1 = np.array(Y1)
ey1 = np.array(DeltaY1)

#mk = 0.49765 #GeV Ks0
mk = 1.11568 #GeV L, Lbar
nPar = 3
nCHAN = 150
length = 7.5

'''
#Tsallis distr
'''
def Tsallis(pT, par):
	Area, Temper, Q = par[0], par[1], par[2]
	return Area*pT*pow( (1 + (Q-1)*((mk**2 + pT**2)**(0.5) - mk)/Temper) , (-1/(Q-1)) )

#------------------------------------------------------------------------------------------------------1

def FCNchi1(npar, gin, f, par, iflag):
	global valFCN1
	yTheor = np.array([Tsallis(i, par) for i in x]) 
	indPos = y1 > 0
	arrayFCN = (  (y1[indPos] - yTheor[indPos])/ey1[indPos] )**2
	valFCN1 = np.sum(arrayFCN)
	f.value = valFCN1

'''
#MIUNIT
'''
minuit1 = ROOT.TMinuit(5)
minuit1.SetPrintLevel(1)
minuit1.SetFCN(FCNchi1)
errordef = 1.

# Chi square start parameters

minuit1.DefineParameter(0, 'Area', 10.2, 1e-4, 0., 0.)
minuit1.DefineParameter(1, 'Temper', 0.65, 1e-4, 0., 0.)
minuit1.DefineParameter(2, 'Q', 1.14, 1e-3, 0., 0.)

ierflg = ctypes.c_int(0)
minuit1.mncomd("SET ERR " + str(1), ierflg)
minuit1.mncomd("SET STR 1", ierflg)
minuit1.mncomd("MIGRAD 100000 1e-8", ierflg)

NDF1 = nChan - minuit1.GetNumFreePars()
print("\nChi/NDF = ", valFCN1, '/', NDF1)

valPar1 = ctypes.c_double(0)
errPar1 = ctypes.c_double(0)
	 
parFit1 = np.zeros(5)
parErr1 = np.zeros(5)
	
for i in range(nPar):
	minuit1.GetParameter(i, valPar1, errPar1)
	parFit1[i] = valPar1.value
	parErr1[i] = errPar1.value

X1 = np.linspace(0, length, nCHAN)
dx1 = X1[1] - X1[0]
DeltaX1 = [dx1]*len(X1)
Y_1 = np.array([Tsallis(i, parFit1) for i in X1])
Ynew1 = np.array([Tsallis(i, parFit1)*i**2 for i in X1])

print('\n \n \n \n')

#------------------------------------------------------------------------------------------------------2
'''
AREAS
'''
def findArea(x, xerr, y): # find an area under histogram
	Area = 0 
	for i in range(len(x)):
		Area = Area + 2*xerr[i]*y[i]
	return Area

#normal areas
A1 = findArea(x, ex, y1)
print('\nnormal areas 1\n',A1)

#normal areas with X
A_1 = findArea(X1, DeltaX1, Y_1)
print('normal areas with X 1\n',A_1)

# pT**2 * f(pT) areas
Anew1 = findArea(X1, DeltaX1, Ynew1)
print('pT**2 * f(pT) areas 1\n',Anew1)

'''
T init
'''
Tinit1 = np.sqrt( (Anew1/A_1)/2 )
print('<pT**2> 1\n',Anew1/A_1)
print('T init 1\n',Tinit1)


#---------------------------------------------------------------------------------------------------PLOT

c1 = TCanvas( 'c1', 'A Simple Graph Example',500, 500 )
'''
PLOT
'''
ROOT.gStyle.SetOptStat(0)
Plot1 = ROOT.TGraphErrors(nChan, x, y1, ex, ey1)
Plot1.SetMarkerStyle(20)
Plot1.SetMarkerColor(ROOT.kRed)
Plot1.SetMarkerSize(1.1)
Plot1.SetLineWidth(3)
Plot1.GetXaxis().SetTitle('#it{p}_{T} [GeV/c]')
Plot1.GetXaxis().SetTitleSize(0.05)
Plot1.GetXaxis().SetTitleOffset(1.00)
Plot1.GetXaxis().SetLabelSize(0.05)

#Plot1.GetYaxis().SetTitle(' \\frac{\partial \sigma}{ \partial p_{T}} [\\frac{mb}{GeV/c}]')
Plot1.GetYaxis().SetTitle('#frac{#partial^{2}#sigma}{#partialp_{T}#partialy} [mb/(GeV/c)]')
Plot1.GetYaxis().SetTitleSize(0.05)
Plot1.GetYaxis().SetTitleOffset(1.25)
Plot1.GetYaxis().SetLabelSize(0.05)

#Plot1.SetTitle("K_{s}^{0} pp #sqrt{s_{NN}}= 5.02 TeV")
#Plot1.SetTitle("K_{s}^{0}, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")

Plot1.SetTitle(" ")
#Plot1.SetTitle("#Lambda, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")

#Plot1.SetTitle("#bar{#Lambda}, LHCb p-p #sqrt{s_{NN}}= 5.02 TeV")
#Plot1.SetTitle("#bar{#Lambda}, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")

fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X1 - dx1/2.)
fFit1.SetLineColor(ROOT.kRed)
fFit1.SetLineWidth(2)
fFit1.SetLineStyle(1)

for chan in range(nCHAN):
    fFit1.SetBinContent(chan + 1 ,Y_1[chan])

#------------------------------------------------------------------------------------------------------2



Legend = ROOT.TLegend(0.45,0.88,0.93,0.73)
Legend.SetHeader('#Lambda p-p #sqrt{s_{NN}}= 5.02 TeV', 'C')
Legend.AddEntry(fFit1,'Tsallis, T_{init}= 0.867 GeV', 'l')
Legend.AddEntry(Plot1, '2.0 < y < 4.0', 'lep')
Legend.SetTextAlign(12)
Legend.SetTextSize(0.04)
Legend.SetFillStyle(0)
Legend.SetLineWidth(0)


Legend1 = ROOT.TLegend(0.33,0.87,0.43,0.77)
Legend1.SetHeader('LHCb', 'C')
Legend1.SetTextAlign(12)
Legend1.SetTextSize(0.05)
Legend1.SetFillStyle(0)
Legend1.SetLineWidth(0)
Legend1.SetTextFont(4)






ROOT.gPad.SetLogy(1)
ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

Plot1.Draw("AP")
fFit1.Draw("SAME&l")

Legend1.Draw("SAME")
Legend.Draw("SAME")
#Legend2.Draw("SAME")
#labelLHCb.Draw("SAME")


time.sleep(60)
ROOT.gPad.Update()
c1.Update()
