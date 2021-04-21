import ROOT

fl = ROOT.TFile('mult_kin_hst.root', 'open')
keys = fl.GetListOfKeys()
names = [x.GetName() for x in keys]
print(names, '\n')

hst = {x: fl.Get(x) for x in names}
print(hst, '\n')

print(hst{'pPb Down pt nspd 0'})
fl.Close()
