import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes


DATA = ['nspd(0,1).txt']

x1 = [0]*13
y1 = [0]*13

nChan1 = 13

nCHAN = 150
length = 13.0

Y1 = [0]*nCHAN

Ynew1 = [0]*nCHAN

ex1 = [0]*13
ey1 = [0]*13

exRight1 = [0]*len(x1)
exLeft1 = [0]*len(x1)

chi1 = 0

NDF1 = 0

mk = 0.497648 #GeV
nPar = 3



def findArea(x, xerr, y): # find an area under histogram
	Area = 0 
	for i in range(len(x)):
		Area = Area + 2*xerr[i]*y[i]
	return Area
	
	
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
		        xLow01[i] = xLow01Reper[j]
		        xTop01[i] = xTop01Reper[j]
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
		#arrayFCN = (y01[indPos] - yTheor[indPos])**2/y01[indPos]
		
		arrayFCN = (  (y01[indPos] - yTheor[indPos])  /  Deltay01[indPos] )**2  #''' correct chi '''
		
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
	print("Chi/NDF = ", valFCN, '/', NDF)
	 
	valPar = ctypes.c_double(0)
	errPar = ctypes.c_double(0)
	 
	parFit = np.zeros(5)
	parErr = np.zeros(5)
	
	for i in range(nPar):
		minuit.GetParameter(i, valPar, errPar)
		parFit[i] = valPar.value
		parErr[i] = errPar.value



	#nCHAN = 50
	X = np.linspace(0, length ,nCHAN)
	dx = X[1] - X[0]
	Y = np.array([Tsallis(i, parFit) for i in X])
	Ynew =  np.array([Tsallis(i, parFit)*i**2 for i in X])

		
	if I == 0:
		x1 = x01
		y1 = y01
		Y1 = Y
		Ynew1 = Ynew
		ex1 = Deltax01
		ey1 = Deltay01
		exLeft1 = xLow01
		exRight1 = xTop01
		chi1 = valFCN
		NDF1 = NDF

		
	I = I + 1
	



'''
PLOT
'''
ROOT.gStyle.SetOptStat(0)




X = np.linspace(0, length, nCHAN)
dx = X[1] - X[0]
DeltaX = [dx]*len(X)
#Xnew  =  np.array([i**2  for i in X])












#Err1 = ROOT.TGraphAsymmErrors(nChan1 , xnew1, y1, exLeft1, exRight1, ey1, ey1)
Err1 = ROOT.TGraphErrors(nChan1 - 1, x1, y1, ex1, ey1)
Err1.SetMarkerStyle(20)
Err1.SetMarkerColor(ROOT.kBlack)
Err1.SetMarkerSize(1.0)
Err1.SetLineWidth(1)
Err1.GetXaxis().SetTitle('p_{T}^{2} [GeV^{2}/c^{2}]')
Err1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Err1.SetTitle("LHCb p-Pb 8 TeV")

fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X - dx/2.)
#fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit1.SetLineColor(ROOT.kBlack)
fFit1.SetLineWidth(2)
fFit1.SetLineStyle(2)

for chan in range(nCHAN):
    fFit1.SetBinContent(chan + 1 ,Y1[chan])








'''
AREAS
'''
#normal areas
A1 = findArea(x1, ex1, y1)

print('\n \n \n normal areas \n',A1)

#normal areas with X
A_1 = findArea(X, DeltaX, Y1)

print('\n \n \n normal areas with X \n',A_1)

# pT**2 * f(pT) areas
Anew1 = findArea(X, DeltaX, Ynew1)


print('\n \n pT**2 * f(pT) areas \n',Anew1)

'''
T init
'''
Tinit1 = np.sqrt( (Anew1/A_1)/2 )

print('\n \n <pT**2> \n',Anew1/A_1)
print('\n \n T init \n',Tinit1)








Err1.Draw("AP")
fFit1.Draw("SAME&l")

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(30)
ROOT.gPad.Update()
