import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes


#DATA = 'ppKs05TeVOnceNEW.txt'
#DATA = 'ppKs05TeVDoubleNEW.txt'

#DATA = 'ppLambda5TeVOnceNEW.txt'
#DATA = 'ppLambda5TeVDoubleNEW.txt'

#DATA = 'ppLambdaBar5TeVOnceNEW.txt'
DATA = 'ppLambdaBar5TeVDoubleNEW.txt'

X, Y, DeltaX, DeltaY = np.loadtxt(DATA, unpack=True)
nChan = len(X)

x = np.array(X)
y = np.array(Y)
ex = np.array(DeltaX)
ey = np.array(DeltaY)

#print(X,'\n' ,DeltaX,'\n' , Y,'\n' , DeltaY, '\n \n')
#print(x,'\n' ,ex,'\n' , y,'\n' , ey, '\n \n')

mk = 0.49765 #GeV Ks0
#mk = 1.11568 #GeV L, Lbar
nPar = 3
nCHAN = 150
length = 6.0


'''
#Tsallis distr
'''

def Tsallis(pT, par):
	Area, Temper, Q = par[0], par[1], par[2]
	return Area*pT*pow( (1 - (1-Q)*((mk**2 + pT**2)**(0.5) - mk)/Temper) , (1/(1-Q)) )

'''
def Tsallis(pT, par):
	Area1, Area2,Temper1, Temper2, n1, n2, k = par[0], par[1], par[2], par[3], par[4], par[5], par[6]
	
	return Area1*k*pT*pow((1 + ((mk**2 + pT**2)**(0.5) - mk)/(Temper1*n1) , (-n1)))     +   Area2*(1-k)*pT*pow((1 + ((mk**2 + pT**2)**(0.5) - mk)/(Temper2*n2) , (-n2)))
'''


def FCNchi(npar, gin, f, par, iflag):
	global valFCN
	yTheor = np.array([Tsallis(i, par) for i in x]) 
	indPos = y > 0
	arrayFCN = (  (y[indPos] - yTheor[indPos])/ey[indPos] )**2
	valFCN = np.sum(arrayFCN)
	f.value = valFCN

'''
#MIUNIT
'''
minuit = ROOT.TMinuit(5)
minuit.SetPrintLevel(1)
minuit.SetFCN(FCNchi)
errordef = 1.

# Chi square start parameters

minuit.DefineParameter(0, 'Area', 7, 1e-4, 0., 0.)
minuit.DefineParameter(1, 'Temper', 0.1, 1e-3, 0., 0.)
minuit.DefineParameter(2, 'Q', 1.1, 1e-3, 0., 0.)
'''
minuit.DefineParameter(0, 'Area1', 4, 1e-4, 0., 0.)
minuit.DefineParameter(1, 'Area2', 4, 1e-4, 0., 0.)
minuit.DefineParameter(2, 'Temper1', 0.1, 1e-3, 0., 0.)
minuit.DefineParameter(3, 'Temper2', 0.1, 1e-3, 0., 0.)
minuit.DefineParameter(4, 'n1', 10, 1e-3, 0., 0.)
minuit.DefineParameter(5, 'n2', 10, 1e-3, 0., 0.)
minuit.DefineParameter(6, 'k', 0.9, 1e-3, 0., 0.)
'''

ierflg = ctypes.c_int(0)
minuit.mncomd("SET ERR " + str(1), ierflg)
minuit.mncomd("SET STR 1", ierflg)
minuit.mncomd("MIGRAD 100000 1e-8", ierflg)

NDF = nChan - minuit.GetNumFreePars()
print("\nChi/NDF = ", valFCN, '/', NDF)

valPar = ctypes.c_double(0)
errPar = ctypes.c_double(0)
	 
parFit = np.zeros(5)
parErr = np.zeros(5)
	
for i in range(nPar):
	minuit.GetParameter(i, valPar, errPar)
	parFit[i] = valPar.value
	parErr[i] = errPar.value

X = np.linspace(0, length, nCHAN)
dx = X[1] - X[0]
DeltaX = [dx]*len(X)
Y = np.array([Tsallis(i, parFit) for i in X])
Ynew = np.array([Tsallis(i, parFit)*i**2 for i in X])


'''
AREAS
'''
def findArea(x, xerr, y): # find an area under histogram
	Area = 0 
	for i in range(len(x)):
		Area = Area + 2*xerr[i]*y[i]
	return Area

#normal areas
A1 = findArea(x, ex, y)
print('\n normal areas \n',A1)

#normal areas with X
A_1 = findArea(X, DeltaX, Y)
print('\n normal areas with X \n',A_1)

# pT**2 * f(pT) areas
Anew1 = findArea(X, DeltaX, Ynew)
print('\n pT**2 * f(pT) areas \n',Anew1)

'''
T init
'''
Tinit1 = np.sqrt( (Anew1/A_1)/2 )
print('\n <pT**2> \n',Anew1/A_1)
print('\n T init \n',Tinit1)
print('\n DATA \n',DATA, '\n \n')



'''
PLOT
'''
ROOT.gStyle.SetOptStat(0)
#ROOT.gPad.SetLogy(1)
Plot = ROOT.TGraphErrors(nChan, x, y, ex, ey)
Plot.SetMarkerStyle(21)
Plot.SetMarkerColor(ROOT.kViolet-3)
Plot.SetMarkerSize(1.0)
Plot.SetLineWidth(1)
Plot.GetXaxis().SetTitle('p_{T} [GeV/c]')


#Plot.GetYaxis().SetTitle(' \\frac{\partial \sigma}{ \partial p_{T}} [\\frac{mb}{GeV/c}]')
Plot.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial y} [\\frac{mb}{GeV/c}]')


#Plot.SetTitle("K_{s}^{0}, LHCb p-p #sqrt{s_{NN}}= 5.02 TeV")
#Plot.SetTitle("K_{s}^{0}, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")

#Plot.SetTitle("#Lambda, LHCb p-p #sqrt{s_{NN}}= 5.02 TeV")
#Plot.SetTitle("#Lambda, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")

Plot.SetTitle("#bar{#Lambda}, LHCb p-p #sqrt{s_{NN}}= 5.02 TeV")
#Plot.SetTitle("#bar{#Lambda}, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")



fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit1.SetLineColor(ROOT.kBlack)
fFit1.SetLineWidth(2)
fFit1.SetLineStyle(7)

for chan in range(nCHAN):
    fFit1.SetBinContent(chan + 1 ,Y[chan])
    
'''
Legend = ROOT.TLegend(0.3,0.70,0.90,0.9)
text = '\chi^{2}/NDF = ' +str(valFCN)+ '/' +str(NDF)+ ',T_{init} = ' +str(Tinit1)+ ' GeV'
Legend.AddEntry(Plot,text, ' lep ')
Legend.SetFillColor(0)
Legend.SetTextAlign(12)
Legend.SetTextSize(0.027)
Legend.SetTextFont(2)
'''

Plot.Draw("AP")
fFit1.Draw("SAME&l")
#Legend.Draw("SAME")

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()
time.sleep(60)
ROOT.gPad.Update()
