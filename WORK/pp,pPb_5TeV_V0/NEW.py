import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes


DATA = 'ppKs05TeVOnceNEW.txt'

X, Y, Deltax, Deltay = np.loadtxt(DATA, unpack=True)
N = len(X)

'''
X = [1.,2.,3.,4.,5.]
Y = [1.,2.,3.,4.,5.]
Deltax = [1.,1.,1.,1.,1.]
Deltay = [1.,1.,1.,1.,1.]
N = 5
'''

print(X,'\n' ,Y, '\n', Deltax,'\n',Deltay, '\n \n')

x = np.array(X)
y = np.array(Y)
ex = np.array(Deltax)
ey = np.array(Deltay)
print(x,'\n' ,y, '\n', ex,'\n', ey, '\n \n')


#Plot = ROOT.TGraphErrors(N, X, Y, Deltax, Deltay)

Plot = ROOT.TGraphErrors(N, x, y, ex, ey)

#Plot = ROOT.TGraphErrors('ppKs05TeVOnceNEW.txt')

Plot.SetMarkerStyle(20)
Plot.SetMarkerColor(ROOT.kBlack)
Plot.SetMarkerSize(1.0)
Plot.SetLineWidth(1)
Plot.GetXaxis().SetTitle('p_{T} [GeV/c]')
Plot.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial N} [a.u.]')
Plot.SetTitle("Ks p-p 5 TeV")



Plot.Draw("AP")


ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()

time.sleep(30)
ROOT.gPad.Update()

