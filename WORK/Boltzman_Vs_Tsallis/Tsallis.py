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

Area = 1
pT_max = 10000 #MeV

Q = [0.6, 0.7, 0.8, 0.9]
m = [497.611, 497.611,497.611,497.611] #MeV
T = [200, 200, 200, 200] #MeV

color = [ROOT.kRed, ROOT.kViolet-3, ROOT.kBlue, ROOT.kPink+8]
plots = ['Plot1', 'Plot2', 'Plot3', 'Plot4']

pT = array.array('d',[i for i in range(pT_max)])  #MeV
nchan = len(pT)


#F = array.array('d',[ Area*i*pow((1 + (1-Q[0])*((m[0]**2 + i**2)**(0.5) - m[0])/T[0]),(-1/(1-Q[0]))) for i in pT ])
#Fmax = np.amax(F)
#Fdash = F/Fmax
#---------------------------------------------------------------------------------------------------------------------------

def Tsallis(j):
	F = np.array([ Area*i*pow((1 + (1-Q[j])*((m[j]**2 + i**2)**(0.5) - m[j])/T[j]),(-1/(1-Q[j]))) for i in pT ])
	return F


c1 = TCanvas( 'c1', 'A Simple Graph Example',500, 500 )
ROOT.gStyle.SetOptStat(0)

ROOT.gPad.SetLogy(1)
ROOT.gPad.SetLogx(1)

Ymax = 250
Ymin = 10**(-1)
pT_min = 2*10**2 #MeV

ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()


'''
Plot1 = ROOT.TGraph(nchan, pT, Tsallis(0))
Plot1.SetLineColor(color[0])
Plot1.SetLineWidth(3)
Plot1.GetXaxis().SetTitle('#it{p}_{T} [MeV/c]')
Plot1.GetXaxis().SetTitleSize(0.04)
Plot1.GetXaxis().SetTitleOffset(1.00)
Plot1.GetXaxis().SetLabelSize(0.04)
Plot1.GetXaxis().SetRangeUser(0,10000)

Plot1.GetYaxis().SetTitle('#it{f(p_{T})}')
Plot1.GetYaxis().SetTitleSize(0.04)
Plot1.GetYaxis().SetTitleOffset(1.00)
Plot1.GetYaxis().SetLabelSize(0.04)
Plot1.GetYaxis().SetRangeUser(10**(-4),400)

Plot1.SetTitle(" ")
Plot1.Draw("A&l")
'''


for j in range(4):
	F = Tsallis(j)
	
	plots[j] = ROOT.TGraph(nchan, pT, F)
	plots[j].SetLineColor(color[j])
	plots[j].SetLineWidth(2)
	plots[j].GetXaxis().SetTitle('#it{p}_{T} [MeV/c]')
	plots[j].GetXaxis().SetTitleSize(0.04)
	plots[j].GetXaxis().SetTitleOffset(1.00)
	plots[j].GetXaxis().SetLabelSize(0.04)
	plots[j].GetXaxis().SetRangeUser(pT_min,pT_max)
	plots[j].GetYaxis().SetTitle('#it{f(p_{T})}')
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



