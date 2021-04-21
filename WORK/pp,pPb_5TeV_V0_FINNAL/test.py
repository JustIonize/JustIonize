import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
from ROOT import TCanvas, TGraph, TPaveLabel, TLatex
from ROOT import gROOT
import matplotlib.pyplot as plt
import ctypes

x = [1,2,3,4,5]
N = len(x)


def DX(i):
	return x[i]

DONE = 0
for i in range (0,N):
	#print(i)
	#print(DX(i), '\n')
	DONE = DONE + DX(i)
	
print('DONE :', DONE)
print('DONE real:', sum(x))
