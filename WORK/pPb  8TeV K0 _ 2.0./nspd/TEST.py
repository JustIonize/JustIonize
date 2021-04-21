import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes



h = ROOT.TH1F("h","h",10,0,10)
h.Fill(1)
h.Integral(2,2)
h.Integral(1,2)
h.Integral(2,1)
h.Integral(3,1)

print(h.Integral(2,2))

#h.SetLineColor(ROOT.kBlack)
#h.SetLineWidth(3)
#h.Draw("AP")


time.sleep(10)
ROOT.gPad.Update()
