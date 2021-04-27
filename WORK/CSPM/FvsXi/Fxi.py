import sys, time
import numpy as np
import matplotlib.pyplot as plt 
import ctypes
import array

import ROOT
from ROOT import TMinuit
from ROOT import TCanvas, TGraph, TPaveLabel, TLatex
from ROOT import gROOT
from ROOT import TFormula, TF1
from ROOT import gObjectTable


plotNum = 4

xi_max = 1.3
xi_min = 10**(-6)
nchan = 10**(4)

color = [ROOT.kRed, ROOT.kViolet-3, ROOT.kBlue, ROOT.kPink+8]
plots = ['Plot1', 'Plot2', 'Plot3', 'Plot4']
#ro  = [5*10**(30), 6.66*10**(30), 8.33*10**(30), 10*10**(30)]
#r02 = [0.2, 0.217, 0.233 , 0.25]
#xi = np.linspace(xi_min,xi_max,nchan)


#def xi(x,y):
#	return x*np.pi*y**2
def F(x):
	return np.sqrt( (1 - np.exp(-x)) / x )




c1 = TCanvas( 'c1', 'A Simple Graph Example',500, 500 )
ROOT.gStyle.SetOptStat(0)

Ymax = 1.02
Ymin = 7.4*10**(-1)

#ROOT.gPad.SetLogy(1)
#ROOT.gPad.SetLogx(1)

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()


for j in range(plotNum):
	
	Func = F(xi)
	
	plots[j] = ROOT.TGraph(nchan, xi , Func)
	plots[j].SetLineColor(color[j])
	plots[j].SetLineWidth(2)
	plots[j].GetXaxis().SetTitle('#xi = #rho#pir_{0}^{2} ')
	plots[j].GetXaxis().SetTitleSize(0.04)
	plots[j].GetXaxis().SetTitleOffset(1.05)
	plots[j].GetXaxis().SetLabelSize(0.04)
	plots[j].GetXaxis().SetRangeUser(xi_min,xi_max)
	plots[j].GetYaxis().SetTitle('F(#xi)')
	plots[j].GetYaxis().SetTitleSize(0.04)
	plots[j].GetYaxis().SetTitleOffset(1.00)
	plots[j].GetYaxis().SetLabelSize(0.04)
	plots[j].GetYaxis().SetRangeUser(Ymin,Ymax)
	plots[j].SetTitle(" ")
	
	if j == 0:
		plots[j].Draw("A&l")
	else:
		plots[j].Draw("SAME&l")	


time.sleep(30)
ROOT.gPad.Update()
c1.Update()
#---------------------------------------------------------------------------------------------------------------------------
