import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes


DATA = ['ppKs05TeVOnce.txt']

x1 = [0]*15
y1 = [0]*15

nChan1 = 15
nCHAN = 50
length = 6.0

Y1 = [0]*nCHAN

Ynew1 = [0]*nCHAN

ex1 = [0]*15
ey1 = [0]*15

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
	

for name in DATA:
	
	x01, Deltax01, y01, Deltay01 = np.loadtxt(name, unpack=True)
	x01 = x01/1000
	nChan = len(x01)
	
	print(x01,'\n' ,Deltax01,'\n' , y01,'\n' , Deltay01, '\n \n')
	
	
	'''
	Tsallis distr
	'''
	def Tsallis(pT, par):
		Area, Temper, Q = par[0], par[1], par[2]
		return Area*pT*pow( (1 + (Q-1)*((mk**2 + pT**2)**(0.5) - mk)/Temper) , (-1/(Q-1)) )
		
		
		
		
		
	'''
	#FCN for chi
	'''
	def FCNchi(npar, gin, f, par, iflag):
		global valFCN
		yTheor = np.array([Tsallis(i, par) for i in x01]) 
		#print(' yTheor', yTheor, '\n')
		indPos = y01 > 0
		arrayFCN = (  (y01[indPos] - yTheor[indPos])/Deltay01[indPos] )**2
		#print(' arrayFCN', arrayFCN, '\n')
		valFCN = np.sum(arrayFCN)
		#print(' valFCN', valFCN, '\n')
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
	errordef = 1.

	# Chi square start parameters
	minuit.DefineParameter(0, 'Area', 30, 1e-1, 0., 0.)
	minuit.DefineParameter(1, 'Temper', 0.5, 1e-3, 0., 0.)
	minuit.DefineParameter(2, 'Q', 1.1, 1e-3, 0., 0.)

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


	X = np.linspace(0, length ,nCHAN)
	dx = X[1] - X[0]
	Y = np.array([Tsallis(i, parFit) for i in X])

	x1 = x01
	y1 = y01
	Y1 = Y
	ex1 = Deltax01
	ey1 = Deltay01

	



'''
PLOT
'''
ROOT.gStyle.SetOptStat(0)



X = np.linspace(0, length, nCHAN)
dx = X[1] - X[0]


Err1 = ROOT.TGraphErrors(nChan1 - 1, x1, y1, ex1, ey1)

Err1.SetMarkerStyle(20)
Err1.SetMarkerColor(ROOT.kBlack)
Err1.SetMarkerSize(1.0)
Err1.SetLineWidth(1)
Err1.GetXaxis().SetTitle('p_{T} [GeV/c]')
Err1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Err1.SetTitle("Ks p-p 5 TeV")

fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X - dx/2.)
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
