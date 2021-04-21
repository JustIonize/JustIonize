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

nCHAN = 150
length = 13.0

Y1 = [0]*nCHAN
Y2 = [0]*nCHAN
Y3 = [0]*nCHAN

Ynew1 = [0]*nCHAN
Ynew2 = [0]*nCHAN
Ynew3 = [0]*nCHAN
 

ex1 = [0]*13
ex2 = [0]*14
ex3 = [0]*14

ey1 = [0]*13
ey2 = [0]*14
ey3 = [0]*14

exRight1 = [0]*len(x1)
exLeft1 = [0]*len(x1)
exRight2 = [0]*len(x2)
exLeft2 = [0]*len(x2)
exRight3 = [0]*len(x3)
exLeft3 = [0]*len(x3)

chi1 = 0
chi2 = 0
chi3 = 0

NDF1 = 0
NDF2 = 0
NDF3 = 0

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
	'''
	if len(x1) == len(x01):
		x1 = x01
		y1 = y01
		Y1 = Y
		ex1 = Deltax01
		ey1 = Deltay01

	if len(x2) == len(x01):
		x2 = x01
		y2 = y01
		Y2 = Y
		ex2 = Deltax01
		ey2 = Deltay01

	if len(x3) == len(x01):
		x3 = x01
		y3 = y01
		Y3 = Y
		ex3 = Deltax01
		ey3 = Deltay01
		'''
		
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

	if I == 1:
		x2 = x01
		y2 = y01
		Y2 = Y
		Ynew2 = Ynew
		ex2 = Deltax01
		ey2 = Deltay01
		exLeft2 = xLow01
		exRight2 = xTop01
		chi2 = valFCN
		NDF2 = NDF
		
	if I == 2:
		x3 = x01
		y3 = y01
		Y3 = Y
		Ynew3 = Ynew
		ex3 = Deltax01
		ey3 = Deltay01
		exLeft3 = xLow01
		exRight3 = xTop01
		chi3 = valFCN
		NDF3 = NDF
		
	I = I + 1
	



'''
PLOT
'''
ROOT.gStyle.SetOptStat(0)

xnew1 = np.array([i**2  for i in x1])
exRight1 = np.array([i**2 for i in exRight1])
exLeft1 = np.array([i**2  for i in exLeft1])

xnew2 = np.array([i**2  for i in x2])
exRight2 = np.array([i**2  for i in exRight2])
exLeft2 = np.array([i**2  for i in exLeft2])

xnew3 = np.array([i**2  for i in x3])
exRight3 = np.array([i**2  for i in exRight3])
exLeft3 = np.array([i**2  for i in exLeft3])


for j in range(len(xnew1)):
	exRight1[j] =  exRight1[j] - xnew1[j]
	exLeft1[j] = xnew1[j] - exLeft1[j]
	
for j in range(len(xnew2)):
	exRight2[j] =  exRight2[j] - xnew2[j]
	exLeft2[j] = xnew2[j] - exLeft2[j]
	
for j in range(len(xnew3)):
	exRight3[j] =  exRight3[j] - xnew3[j]
	exLeft3[j] = xnew3[j] - exLeft3[j]




X = np.linspace(0, length, nCHAN)
dx = X[1] - X[0]
DeltaX = [dx]*len(X)
Xnew  =  np.array([i**2  for i in X])












Err1 = ROOT.TGraphAsymmErrors(nChan1 , xnew1, y1, exLeft1, exRight1, ey1, ey1)
#Err1 = ROOT.TGraphErrors(nChan1 - 1, x1, y1, ex1, ey1)
Err1.SetMarkerStyle(20)
Err1.SetMarkerColor(ROOT.kBlack)
Err1.SetMarkerSize(1.0)
Err1.SetLineWidth(1)
Err1.GetXaxis().SetTitle('p_{T}^{2} [GeV^{2}/c^{2}]')
Err1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Err1.SetTitle("LHCb p-Pb 8 TeV")

fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, Xnew - dx/2.)
#fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit1.SetLineColor(ROOT.kBlack)
fFit1.SetLineWidth(2)
fFit1.SetLineStyle(2)

for chan in range(nCHAN):
    fFit1.SetBinContent(chan + 1 ,Y1[chan])



Err2 = ROOT.TGraphAsymmErrors(nChan2 , xnew2, y2, exLeft2, exRight2, ey2, ey2)
#Err2 = ROOT.TGraphErrors(nChan2 - 1, x2, y2, ex2, ey2)
Err2.SetMarkerStyle(21)
Err2.SetMarkerColor(ROOT.kViolet)
Err2.SetMarkerSize(1.0)
Err2.SetLineWidth(1)
#Err2.SetLineColor(ROOT.kViolet)

fFit2 = ROOT.TH1F('tsallis2','Data VS Tsallis', nCHAN - 1, Xnew - dx/2.)
#fFit2 = ROOT.TH1F('tsallis2','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit2.SetLineColor(ROOT.kViolet)
fFit2.SetLineWidth(2)
fFit2.SetLineStyle(9)

for chan in range(nCHAN):
    fFit2.SetBinContent(chan + 1 ,Y2[chan])


Err3 = ROOT.TGraphAsymmErrors(nChan3 , xnew3, y3, exLeft3, exRight3, ey3, ey3)
#Err3 = ROOT.TGraphErrors(nChan3 - 1, x3, y3, ex3, ey3)
Err3.SetMarkerStyle(22)
Err3.SetMarkerColor(ROOT.kBlue)
Err3.SetMarkerSize(1.2)
Err3.SetLineWidth(1)

fFit3 = ROOT.TH1F('tsallis3','Data VS Tsallis', nCHAN - 1, Xnew - dx/2.)
#fFit3 = ROOT.TH1F('tsallis3','Data VS Tsallis', nCHAN - 1, X - dx/2.)
fFit3.SetLineColor(ROOT.kBlue)
fFit3.SetLineWidth(2)

for chan in range(nCHAN):
    fFit3.SetBinContent(chan + 1 ,Y3[chan])










'''
AREAS
'''
#normal areas
A1 = findArea(x1, ex1, y1)
A2 = findArea(x2, ex2, y2)
A3 = findArea(x3, ex3, y3)
print('\n \n \n normal areas \n',A1,'\n',A2,'\n',A3)

#normal areas with X
A_1 = findArea(X, DeltaX, Y1)
A_2 = findArea(X, DeltaX, Y2)
A_3 = findArea(X, DeltaX, Y3)
print('\n \n \n normal areas with X \n',A_1,'\n',A_2,'\n',A_3)

# pT**2 * f(pT) areas
Anew1 = findArea(X, DeltaX, Ynew1)
Anew2 = findArea(X, DeltaX, Ynew2)
Anew3 = findArea(X, DeltaX, Ynew3)

print('\n \n pT**2 * f(pT) areas \n',Anew1,'\n',Anew2,'\n',Anew3)

'''
T init
'''
Tinit1 = np.sqrt( (Anew1/A_1)/2 )
Tinit2 = np.sqrt( (Anew2/A_2)/2 )
Tinit3 = np.sqrt( (Anew3/A_3)/2 )

print('\n \n <pT**2> \n',Anew1/A_1,'\n',Anew2/A_2,'\n',Anew3/A_3)
print('\n \n T init \n',Tinit1,'\n',Tinit2,'\n',Tinit3)







Legend = ROOT.TLegend(0.3,0.70,0.90,0.9)

Legend.AddEntry(Err1,'0 < nspd < 100 ,\chi^{2}/NDF = 2.42/10,T_{init} = 0.605 GeV', ' lep ')
Legend.AddEntry(Err2,'200 < nspd < 300 ,\chi^{2}/NDF = 0.52/11 ,T_{init} =0.812 GeV', ' lep ')
Legend.AddEntry(Err3,'400 < nspd < 500 ,\chi^{2}/NDF = 3.38/11 ,T_{init} = 0.838 GeV', ' lep ')

#Legend.SetBorderSize(1)
#Legend.SetFillColor(0)
#Legend.SetTextSize(0.)
#Legend.SetFont(42)

Legend.SetFillColor(0)
Legend.SetTextAlign(12)
Legend.SetTextSize(0.027)
Legend.SetTextFont(2)
#Legend.SetFontStyle(4)

Err1.Draw("AP")
fFit1.Draw("SAME&l")
Err2.Draw("P&SAME")
fFit2.Draw("SAME&l")
Err3.Draw("P&SAME")
fFit3.Draw("SAME&l")

Legend.Draw("SAME")

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(180)
ROOT.gPad.Update()
