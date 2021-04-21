import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
from ROOT import TCanvas, TGraph, TPaveLabel, TLatex
from ROOT import gROOT
import matplotlib.pyplot as plt
import ctypes


DATA = 'ppK2Yint.txt'
X, DeltaX, Y1, DeltaY1 = np.loadtxt(DATA, unpack=True)
nChan = len(X)

x = np.array(X)
ex = np.array(DeltaX)
y1 = np.array(Y1)
ey1 = np.array(DeltaY1)

mk = 0.49765 #GeV Ks0
#mk = 1.11568 #GeV L, Lbar
nPar = 3
nCHAN = 200
length = 7.5

'''
#Tsallis distr
'''

def Tsallis(pT, par):
	Area, Temper, Q = par[0], par[1], par[2]
	return Area*pT*pow( (1 + (Q-1)*((mk**2 + pT**2)**(0.5) - mk)/Temper) , (-1/(Q-1)) )

#-----------------------------------------------------------------------------------------------------------

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
dx1 = (X1[1] - X1[0])/2
DeltaX1 = [dx1]*len(X1)
Y_1 = np.array([Tsallis(i, parFit1) for i in X1])
Ynew1 = np.array([Tsallis(i, parFit1)*i**2 for i in X1])






print('\n \n \n \n')
print('The parameters are : \n', parFit1[0],' +-', parErr1[0],'\n' ,parFit1[1],' +- ', parErr1[1],'\n' ,parFit1[2],' +- ', parErr1[2],'\n\n' )
#------------------------------------------------------------------------------------------------------AREAS


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
PT2 = Anew1/A_1
Tinit1 = np.sqrt( (PT2)/2 )
print('<pT**2> 1\n',PT2)
print('T init 1\n',Tinit1)
#print('\n DATA \n',DATA, '\n \n')



#-------------------------------------------------------------------------------------------------------Error


'''
#DX
'''
pT = X1
DpT = DeltaX1

A = parFit1[0]
DA = parErr1[0]

Temper = parFit1[1]
DT = parErr1[1]

q = parFit1[2]
Dq = parErr1[2]


#print('\n\npT :', pT, '\n', 'A :', A, '\n','T :', Temper, '\n', 'q :', q, '\n') 
print('\n\nA :', A, '\n','T :', Temper, '\n', 'q :', q, '\n') 
print('DpT :', DeltaX1[0], '\n', 'Dq :', parErr1[2], '\n','DT :', parErr1[1], '\n', 'DA :',parErr1[0], '\n') 



def dxdpT(i):
	return  2*DpT[0]*3*pT[i]**2*A*pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)) )     +     2*DpT[0]*pT[i]**3*A*(-1/(q-1))*pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1) - 1) ) * ( (q-1)*(mk**2 + pT[i]**2)**(-0.5)*pT[i]/Temper )
def dxdq(i):
	return 2*DpT[0]*A*pT[i]**3 * ( np.log( 1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper ) * pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)) ) * (((mk**2+pT[i]**2)**(0.5)-mk)/Temper)   )
def dxdT(i):
	return 2*DpT[0]*A*pT[i]**3 * (-1/(q-1)) * pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)-1) ) * ( - (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper**2 )
def dxdA(i):
	return 2*DpT[0]*pT[i]**3*pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)) )

def DX(i):
	return np.sqrt( dxdpT(i)**2*DpT[i]**2 + dxdq(i)**2*Dq**2 + dxdT(i)**2*DT**2 + dxdA(i)**2*DA**2)


'''
#ONE
'''
ONE = Anew1
N = nCHAN
DONE = 0
for i in range (0,N):
	DONE = DONE + DX(i)
	
print('\n\nArea 1 = ', Anew1, ' +- ', DONE, '\n\n')
#print('\n', 2*DeltaX1[20]*Ynew1[20], ' +- ' , DX(20))


'''
#DY
'''

pT = X1
DpT = DeltaX1

A = parFit1[0]
DA = parErr1[0]

Temper = parFit1[1]
DT = parErr1[1]

q = parFit1[2]
Dq = parErr1[2]


def dydpT(i):
	return  2*DpT[0]*A*pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)) )     +     2*DpT[0]*pT[i]*A*(-1/(q-1))*pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1) - 1) ) * ( (q-1)*(mk**2 + pT[i]**2)**(-0.5)*pT[i]/Temper )
def dydq(i):
	return 2*DpT[0]*A*pT[i]* ( np.log( 1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper ) * pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)) ) * (((mk**2+pT[i]**2)**(0.5)-mk)/Temper)   )
def dydT(i):
	return 2*DpT[0]*A*pT[i] * (-1/(q-1)) * pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)-1) ) * ( - (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper**2 )
def dydA(i):
	return 2*DpT[0]*pT[i]*pow( (1 + (q-1)*((mk**2 + pT[i]**2)**(0.5) - mk)/Temper) , (-1/(q-1)) )

def DY(i):
	return np.sqrt( dydpT(i)**2*DpT[i]**2 + dydq(i)**2*Dq**2 + dydT(i)**2*DT**2 + dydA(i)**2*DA**2)


'''
#TWO
'''

TWO = A_1
DTWO = 0 
for i in range (0,N):
	DTWO = DTWO + DY(i)
	
print('\n \nArea 2 = ', A_1, ' +- ', DTWO, '\n \n')


'''
#D<pT2>
'''
DpT2 = np.sqrt( (1 / TWO)**2 * DONE**2 + (ONE / TWO**2)**2 * DTWO**2 )

print('\n\n<pT2>', PT2,' +- ',  DpT2 )





'''
#DTinit
'''

DTinit = DpT2 / np.sqrt( 2* PT2 )

print('\n\nTinit', Tinit1,' +- ',  DTinit )

#-------------------------------------------------------------------------------------------WRITE TO TXT

f = open("ppK2FixedRESULTS.txt", "w")
f.write('y range	q	T GeV	Ti GeV	chi/NDF\n')
f.write('New line	' + str(q) + '+-' + str(Dq) + '	' +str(Temper) + '+-' + str(DT) + '	' +str(Tinit1) + '+-' + str(DTinit) + '	' +str(valFCN1) +'/'+str(NDF1) +'\n')
f.close()


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

#TFrame.SetLineWidth(2)



Plot1.GetXaxis().SetTitle('#it{p}_{T} [GeV/c]')
Plot1.GetXaxis().SetTitleSize(0.05)
Plot1.GetXaxis().SetTitleOffset(1.00)
#Plot1.GetXaxis().SetLineWidth(2)
Plot1.GetXaxis().SetLabelSize(0.05)

Plot1.GetYaxis().SetTitle('#frac{#partial^{2}#sigma}{#partialp_{T}#partialy} [mb/(GeV/c)]')
#Plot1.GetYaxis().SetTitle(' \\frac{\partial \sigma}{ \partial p_{T}} [\\frac{mb}{GeV/c}]')
#Plot1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial y} [mb/(GeV/c)]')
Plot1.GetYaxis().SetTitleSize(0.05)
Plot1.GetYaxis().SetTitleOffset(1.25)
Plot1.GetYaxis().SetLabelSize(0.05)



Plot1.SetTitle(" ")

#Plot1.SetTitle("K_{s}^{0}, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")
#Plot1.SetTitle("#Lambda, LHCb p-p #sqrt{s_{NN}}= 5.02 TeV")
#Plot1.SetTitle("#Lambda, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")
#Plot1.SetTitle("#bar{#Lambda}, LHCb p-p #sqrt{s_{NN}}= 5.02 TeV")
#Plot1.SetTitle("#bar{#Lambda}, LHCb p-Pb #sqrt{s_{NN}}= 5.02 TeV")

fFit1 = ROOT.TH1F('tsallis1','Data VS Tsallis', nCHAN - 1, X1 - dx1/2.)
fFit1.SetLineColor(ROOT.kRed)
fFit1.SetLineWidth(2)
fFit1.SetLineStyle(1)

for chan in range(nCHAN):
    fFit1.SetBinContent(chan + 1 ,Y_1[chan])
    



Legend = ROOT.TLegend(0.45,0.88,0.93,0.73)
Legend.SetHeader('K_{s}^{0} p-p #sqrt{s_{NN}}= 5.02 TeV', 'C')
Legend.AddEntry(fFit1,'Tsallis, T_{init}= 0.677 GeV', 'l')
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


'''
Legend1 = ROOT.TLegend(0.55,0.91,0.96,0.80)
Legend1.AddEntry(fFit1,' ', 'l')
Legend1.SetLineWidth(0)


'''
'''
labelLHCb = TPaveLabel( 3,25,4, 30 , 'LHCb' )
labelLHCb.SetFillColor(0)
labelLHCb.SetTextSize(3)

labelLHCb.SetTextAlign(12)
labelLHCb.SetTextFont(0)
#labelLHCb.SetFillStyle(0)
'''

'''
Legend2 = ROOT.TLegend(0.05,0.10,0.30,0.05)
Legend2.AddEntry('LHCb')
Legend2.SetTextAlign(12)
Legend2.SetTextSize(0.04)
Legend2.SetTextFont(2)
Legend2.SetFillStyle(0)
Legend.SetLineWidth(0)
'''


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
