import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes


DATA = 'nspd(0,1).txt'

x1 = [0]*13
nChan1 = 13
y1 = [0]*13
Y1 = [0]*50
ex1 = [0]*13
ey1 = [0]*13

mk = 0.497648 #GeV
nPar = 3

#x01, Deltax01, y01, Deltay01 = np.loadtxt(DATA, unpack=True)



#----------------------------------------------------------------------------------------
xLow01, xTop01, y01, Deltay01 = np.loadtxt(DATA, unpack=True)
xLow01Reper, xTop01Reper, y01Reper, Deltay01Reper = np.loadtxt(DATA, unpack=True)
x, xTop, y, Deltay = np.loadtxt(DATA, unpack=True)



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
y01 = y01/y01[0] 



#----------------------------------------------------------------------------------------


x1 = x01
y1 = y01
ex1 = Deltax01
ey1 = Deltay01

print(x1, '\n', y1, '\n')
	
ROOT.gStyle.SetOptStat(0)


Err1 = ROOT.TGraphErrors(nChan1, x1, y1, ex1, ey1)



Err1.SetMarkerStyle(20)
Err1.SetMarkerColor(ROOT.kBlack)
Err1.SetMarkerSize(1.3)
Err1.SetLineWidth(2)
Err1.GetXaxis().SetTitle('p_{T} [GeV/c]')
Err1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Err1.SetTitle("LHCb 8 TeV")




Err1.Draw("AP")


ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(10)
ROOT.gPad.Update()


'''

[0.325 0.6   0.75  0.85  0.95  1.05  1.15  1.275 1.425 1.6   1.85  2.25	3.   ] 
 [1.         0.89087346 0.70679422 0.53887433 0.43786964 0.35006482  0.25901557 0.20046257 0.13643784 0.10161933 0.05227746 0.02656484  0.00659727] 
 
 
 
 
 [1.7  0.8  0.9  2.5  1.   0.15 1.2  2.   1.1  1.5  1.35 0.5  0.7 ] 
 [0.39725    4.09484    3.32731776 0.05013182 2.66009968 7.59887748
 1.52329053 0.20186299 1.96822755 0.77219282 1.03677446 6.76963826
 5.37084269] 
'''

