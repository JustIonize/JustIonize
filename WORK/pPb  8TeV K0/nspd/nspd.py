import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes

'''
nspd
'''
DATA = ['nspd(0,1).txt','nspd(2,3).txt','nspd(4,5).txt']

x1 = [0]*13
x2 = [0]*14
x3 = [0]*14

nChan1 = 13
nChan2 = 14
nChan3 = 14

y1 = [0]*13
y2 = [0]*14
y3 = [0]*14

Y1 = [0]*50
Y2 = [0]*50
Y3 = [0]*50

ex1 = [0]*13
ex2 = [0]*14
ex3 = [0]*14

ey1 = [0]*13
ey2 = [0]*14
ey3 = [0]*14

mk = 0.497648 #GeV
nPar = 3

I = 0
for name in DATA:
	print(name)
	xLow01, xTop01, y01, Deltay01 = np.loadtxt(name, unpack=True)
	xLow01Reper, xTop01Reper, y01Reper, Deltay01Reper = np.loadtxt(name, unpack=True)
	x, xTop, y, Deltay = np.loadtxt(name, unpack=True)

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
		
	
	
	Deltay01 = Deltay01/y01[0] #normaized
	#Deltay01Reper = Deltay01Reper/y01[0] #normaized
	
	y01 = y01/y01[0] #normaized
	#y01Reper = y01Reper/y01[0] #normaized

	'''
	Tsallis distr
	'''
	def Tsallis(pT, par):
		Area, Temper, Q = par[0], par[1], par[2]
		return Area*pT*pow( (1 - (1-Q)*((mk**2 + pT**2)**(0.5) - mk)/Temper) , (1/(1-Q)) )
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

	nCHAN = 50
	X = np.linspace(0,4.0,nCHAN)
	dx = X[1] - X[0]
	Y = np.array([Tsallis(i, parFit) for i in X])

		
	if I == 0:
		x1 = x01
		y1 = y01
		Y1 = Y
		ex1 = Deltax01
		ey1 = Deltay01

	if I == 1:
		x2 = x01
		y2 = y01
		Y2 = Y
		ex2 = Deltax01
		ey2 = Deltay01

	if I == 2:
		x3 = x01
		y3 = y01
		Y3 = Y
		ex3 = Deltax01
		ey3 = Deltay01
	I = I + 1
	
ROOT.gStyle.SetOptStat(0)

nCHAN = 50
X = np.linspace(0,4.0,nCHAN)
dx = X[1] - X[0]

Err1 = ROOT.TGraphErrors(nChan1, x1, y1, ex1, ey1)
Err1.SetMarkerStyle(20)
Err1.SetMarkerColor(ROOT.kBlack)
Err1.SetMarkerSize(1.3)
Err1.SetLineWidth(2)
Err1.GetXaxis().SetTitle('p_{T} [GeV/c]')
Err1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Err1.SetTitle("LHCb 8 TeV")

fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit1.SetLineColor(ROOT.kBlack)
fFit1.SetLineWidth(3)

for chan in range(nCHAN):
    fFit1.SetBinContent(chan + 1 ,Y1[chan])

Err2 = ROOT.TGraphErrors(nChan2 - 1, x2, y2, ex2, ey2)
Err2.SetMarkerStyle(21)
Err2.SetMarkerColor(ROOT.kRed)
Err2.SetMarkerSize(1.3)
Err2.SetLineWidth(2)

fFit2 = ROOT.TH1F('tsallis2','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit2.SetLineColor(ROOT.kRed)
fFit2.SetLineWidth(3)

for chan in range(nCHAN):
    fFit2.SetBinContent(chan + 1 ,Y2[chan])


Err3 = ROOT.TGraphErrors(nChan3 - 1, x3, y3, ex3, ey3)
Err3.SetMarkerStyle(22)
Err3.SetMarkerColor(ROOT.kGreen)
Err3.SetMarkerSize(1.3)
Err3.SetLineWidth(2)

fFit3 = ROOT.TH1F('tsallis3','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit3.SetLineColor(ROOT.kGreen)
fFit3.SetLineWidth(3)

for chan in range(nCHAN):
    fFit3.SetBinContent(chan + 1 ,Y3[chan])

Legend = ROOT.TLegend(0.60,0.70,0.90,0.90)

Legend.AddEntry(Err1,'0 < nspd < 100', ' p ')
Legend.AddEntry(Err2,'200 < nspd < 300', ' p ')
Legend.AddEntry(Err3,'400 < nspd < 500', ' p ')
'''
Legend.AddEntry(fFit1,'Fit' , ' l ' )
Legend.AddEntry(fFit2,'Fit' , ' l ' )
Legend.AddEntry(fFit3,'Fit' , ' l ' )
'''
Legend.SetFillColor(0)

Err1.Draw("AP")
fFit1.Draw("SAME&l")
Err2.Draw("P&SAME")
fFit2.Draw("SAME&l")
Err3.Draw("P&SAME")
fFit3.Draw("SAME&l")

Legend.Draw("SAME")

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(10)
ROOT.gPad.Update()
