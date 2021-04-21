import sys, time
from ROOT import TMinuit
import numpy as np
import ROOT
import matplotlib.pyplot as plt
import ctypes


DATA = 'ppK2.txt'


X, DeltaX, Y1, DeltaY1, Y2, DeltaY2, Y3, DeltaY3, Y4, DeltaY4 = np.loadtxt(DATA, unpack=True)
nChan = len(X)

x = np.array(X)
ex = np.array(DeltaX)

y1 = np.array(Y1)
ey1 = np.array(DeltaY1)

y2 = np.array(Y2)
ey2 = np.array(DeltaY2)

y3 = np.array(Y3)
ey3 = np.array(DeltaY3)

y4 = np.array(Y4)
ey4 = np.array(DeltaY4)

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

#------------------------------------------------------------------------------------------------------1

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

minuit1.DefineParameter(0, 'Area', 3.2, 1e-4, 0., 0.)
minuit1.DefineParameter(1, 'Temper', 0.21, 1e-4, 0., 0.)
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

#------------------------------------------------------------------------------------------------------2


def FCNchi2(npar, gin, f, par, iflag):
	global valFCN2
	yTheor = np.array([Tsallis(i, par) for i in x]) 
	indPos = y2 > 0
	arrayFCN = (  (y2[indPos] - yTheor[indPos])/ey2[indPos] )**2
	valFCN2 = np.sum(arrayFCN)
	f.value = valFCN2

'''
#MIUNIT
'''
minuit2 = ROOT.TMinuit(5)
minuit2.SetPrintLevel(1)
minuit2.SetFCN(FCNchi2)
errordef = 1.

# Chi square start parameters

minuit2.DefineParameter(0, 'Area', 3.2, 1e-4, 0., 0.)
minuit2.DefineParameter(1, 'Temper', 0.2, 1e-4, 0., 0.)
minuit2.DefineParameter(2, 'Q', 1.14, 1e-3, 0., 0.)

ierflg = ctypes.c_int(0)
minuit2.mncomd("SET ERR " + str(1), ierflg)
minuit2.mncomd("SET STR 1", ierflg)
minuit2.mncomd("MIGRAD 100000 1e-8", ierflg)

NDF2 = nChan - minuit2.GetNumFreePars()
print("\nChi/NDF = ", valFCN2, '/', NDF2)

valPar2 = ctypes.c_double(0)
errPar2 = ctypes.c_double(0)
	 
parFit2 = np.zeros(5)
parErr2 = np.zeros(5)
	
for i in range(nPar):
	minuit2.GetParameter(i, valPar2, errPar2)
	parFit2[i] = valPar2.value
	parErr2[i] = errPar2.value

X2 = np.linspace(0, length, nCHAN)
dx2 = (X2[1] - X2[0])/2
DeltaX2 = [dx2]*len(X2)
Y_2 = np.array([Tsallis(i, parFit2) for i in X2])
Ynew2 = np.array([Tsallis(i, parFit2)*i**2 for i in X2])

print('\n \n \n \n')
#------------------------------------------------------------------------------------------------------3

def FCNchi3(npar, gin, f, par, iflag):
	global valFCN3
	yTheor = np.array([Tsallis(i, par) for i in x]) 
	indPos = y3 > 0
	arrayFCN = (  (y3[indPos] - yTheor[indPos])/ey3[indPos] )**2
	valFCN3 = np.sum(arrayFCN)
	f.value = valFCN3

'''
#MIUNIT
'''
minuit3 = ROOT.TMinuit(5)
minuit3.SetPrintLevel(1)
minuit3.SetFCN(FCNchi3)
errordef = 1.

# Chi square start parameters

minuit3.DefineParameter(0, 'Area', 2.9, 1e-4, 0., 0.)
minuit3.DefineParameter(1, 'Temper', 0.2, 1e-4, 0., 0.)
minuit3.DefineParameter(2, 'Q', 1.13, 1e-3, 0., 0.)

ierflg = ctypes.c_int(0)
minuit3.mncomd("SET ERR " + str(1), ierflg)
minuit3.mncomd("SET STR 1", ierflg)
minuit3.mncomd("MIGRAD 100000 1e-8", ierflg)

NDF3 = nChan - minuit3.GetNumFreePars()
print("\nChi/NDF = ", valFCN3, '/', NDF3)

valPar3 = ctypes.c_double(0)
errPar3 = ctypes.c_double(0)
	 
parFit3 = np.zeros(5)
parErr3 = np.zeros(5)
	
for i in range(nPar):
	minuit3.GetParameter(i, valPar3, errPar3)
	parFit3[i] = valPar3.value
	parErr3[i] = errPar3.value

X3 = np.linspace(0, length, nCHAN)
dx3 = (X3[1] - X3[0])/2
DeltaX3 = [dx3]*len(X3)
Y_3 = np.array([Tsallis(i, parFit3) for i in X3])
Ynew3 = np.array([Tsallis(i, parFit3)*i**2 for i in X3])

print('\n \n \n \n')
#------------------------------------------------------------------------------------------------------4

def FCNchi4(npar, gin, f, par, iflag):
	global valFCN4
	yTheor = np.array([Tsallis(i, par) for i in x]) 
	indPos = y4 > 0
	arrayFCN = (  (y4[indPos] - yTheor[indPos])/ey4[indPos] )**2
	valFCN4 = np.sum(arrayFCN)
	f.value = valFCN4

'''
#MIUNIT
'''
minuit4 = ROOT.TMinuit(5)
minuit4.SetPrintLevel(1)
minuit4.SetFCN(FCNchi4)
errordef = 1.

# Chi square start parameters

minuit4.DefineParameter(0, 'Area', 7, 1e-4, 0., 0.)
minuit4.DefineParameter(1, 'Temper', 0.1, 1e-3, 0., 0.)
minuit4.DefineParameter(2, 'Q', 1.13, 1e-3, 0., 0.)

ierflg = ctypes.c_int(0)
minuit4.mncomd("SET ERR " + str(1), ierflg)
minuit4.mncomd("SET STR 1", ierflg)
minuit4.mncomd("MIGRAD 100000 1e-8", ierflg)

NDF4 = nChan - minuit4.GetNumFreePars()
print("\nChi/NDF = ", valFCN4, '/', NDF4)

valPar4 = ctypes.c_double(0)
errPar4 = ctypes.c_double(0)
	 
parFit4 = np.zeros(5)
parErr4 = np.zeros(5)
	
for i in range(nPar):
	minuit4.GetParameter(i, valPar4, errPar4)
	parFit4[i] = valPar4.value
	parErr4[i] = errPar4.value

X4 = np.linspace(0, length, nCHAN)
dx4 = (X4[1] - X4[0])/2
DeltaX4 = [dx4]*len(X4)
Y_4 = np.array([Tsallis(i, parFit4) for i in X4])
Ynew4 = np.array([Tsallis(i, parFit4)*i**2 for i in X4])

print('\n \n \n \n')
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
PT21 = Anew1/A_1
Tinit1 = np.sqrt( (PT21)/2 )
print('<pT**2> 1\n',PT21)
print('T init 1\n',Tinit1)
#print('\n DATA \n',DATA, '\n \n')


#normal areas
A2 = findArea(x, ex, y2)
print('\n\nnormal areas 2\n',A2)
#normal areas with X
A_2 = findArea(X2, DeltaX2, Y_2)
print('normal areas with X 2\n',A_2)
# pT**2 * f(pT) areas
Anew2 = findArea(X2, DeltaX2, Ynew2)
print('pT**2 * f(pT) areas 2\n',Anew2)
'''
T init
'''
PT22 = Anew2/A_2
Tinit2 = np.sqrt( (PT22)/2 )
print('<pT**2> 2\n',PT22)
print('T init 2\n',Tinit2)
#print('\n DATA \n',DATA, '\n \n')


#normal areas
A3 = findArea(x, ex, y3)
print('\n \nnormal areas 3\n',A3)
#normal areas with X
A_3 = findArea(X3, DeltaX3, Y_3)
print('normal areas with X 3\n',A_3)
# pT**2 * f(pT) areas
Anew3 = findArea(X3, DeltaX3, Ynew3)
print('pT**2 * f(pT) areas 3\n',Anew3)
'''
T init
'''
PT23 = Anew3/A_3
Tinit3 = np.sqrt( (PT23)/2 )
print('<pT**2> 3\n',PT23)
print('T init 3\n',Tinit3)
#print('\n DATA \n',DATA, '\n \n')


#normal areas
A4 = findArea(x, ex, y4)
print('\n \nnormal areas 4\n',A4)
#normal areas with X
A_4 = findArea(X4, DeltaX4, Y_4)
print('normal areas with X 4\n',A_4)
# pT**2 * f(pT) areas
Anew4 = findArea(X4, DeltaX4, Ynew4)
print('pT**2 * f(pT) areas 4\n',Anew4)
'''
T init
'''
PT24 = Anew4/A_4
Tinit4 = np.sqrt( (PT24)/2 )
print('<pT**2> 4\n',PT24)
print('T init 4\n',Tinit4)
#print('\n DATA \n',DATA, '\n \n')

#-------------------------------------------------------------------------------------------------------Error

#--------------------------------------------------------------------------------------------------1
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
print('\n\nA :', A, '\n','T :', Temper, '\n', 'q :', q) 
print('DpT :', DeltaX1[0], '\n', 'Dq :', parErr1[2], '\n','DT :', parErr1[1], '\n', 'DA :',parErr1[0]) 

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
print('Area 1 = ', Anew1, ' +- ', DONE)
#print('\n', 2*DeltaX1[20]*Ynew1[20], ' +- ' , DX(20))

'''
#DY
'''
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
print('Area 2 = ', A_1, ' +- ', DTWO)

'''
#D<pT2>
'''
DpT2 = np.sqrt( (1 / TWO)**2 * DONE**2 + (ONE / TWO**2)**2 * DTWO**2 )
print('<pT2> =', PT21,' +- ',  DpT2)

'''
#DTinit
'''
DTinit = DpT2 / np.sqrt( 2* PT21 )
print('Tinit =', Tinit1,' +- ',  DTinit )


#-------------------------------------------------------------------------------------------WRITE TO TXT

f = open("ppK2FixedRESULTS.txt", "w")
f.write('y range	q	T GeV	Ti GeV	chi/NDF\n')
f.write('1	' + str(q) + '+-' + str(Dq) + '	' +str(Temper) + '+-' + str(DT) + '	' +str(Tinit1) + '+-' + str(DTinit) + '	' +str(valFCN1) +'/'+str(NDF1) +'\n')
f.close()

#--------------------------------------------------------------------------------------------------2

'''
#DX
'''
pT = X2
DpT = DeltaX2

A = parFit2[0]
DA = parErr2[0]

Temper = parFit2[1]
DT = parErr2[1]

q = parFit2[2]
Dq = parErr2[2]

#print('\n\npT :', pT, '\n', 'A :', A, '\n','T :', Temper, '\n', 'q :', q, '\n') 
print('\n\nA :', A, '\n','T :', Temper, '\n', 'q :', q) 
print('DpT :', DeltaX2[0], '\n', 'Dq :', parErr2[2], '\n','DT :', parErr2[1], '\n', 'DA :',parErr2[0]) 

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
ONE = Anew2
N = nCHAN
DONE = 0
for i in range (0,N):
	DONE = DONE + DX(i)
print('Area 1 = ', Anew2, ' +- ', DONE)
#print('\n', 2*DeltaX1[20]*Ynew1[20], ' +- ' , DX(20))

'''
#DY
'''

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
TWO = A_2
DTWO = 0 
for i in range (0,N):
	DTWO = DTWO + DY(i)
print('Area 2 = ', A_2, ' +- ', DTWO)

'''
#D<pT2>
'''
DpT2 = np.sqrt( (1 / TWO)**2 * DONE**2 + (ONE / TWO**2)**2 * DTWO**2 )
print('<pT2> =', PT22,' +- ',  DpT2)

'''
#DTinit
'''
DTinit = DpT2 / np.sqrt( 2* PT22 )
print('Tinit =', Tinit2,' +- ',  DTinit )



#-------------------------------------------------------------------------------------------WRITE TO TXT

f = open("ppK2FixedRESULTS.txt", "a")
f.write('2	' + str(q) + '+-' + str(Dq) + '	' +str(Temper) + '+-' + str(DT) + '	' +str(Tinit2) + '+-' + str(DTinit) + '	' +str(valFCN2) +'/'+str(NDF2) +'\n')
f.close()

#--------------------------------------------------------------------------------------------------3



'''
#DX
'''
pT = X3
DpT = DeltaX3

A = parFit3[0]
DA = parErr3[0]

Temper = parFit3[1]
DT = parErr3[1]

q = parFit3[2]
Dq = parErr3[2]

#print('\n\npT :', pT, '\n', 'A :', A, '\n','T :', Temper, '\n', 'q :', q, '\n') 
print('\n\nA :', A, '\n','T :', Temper, '\n', 'q :', q) 
print('DpT :', DeltaX3[0], '\n', 'Dq :', parErr3[2], '\n','DT :', parErr3[1], '\n', 'DA :',parErr3[0]) 

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
ONE = Anew3
N = nCHAN
DONE = 0
for i in range (0,N):
	DONE = DONE + DX(i)
print('Area 1 = ', Anew3, ' +- ', DONE)
#print('\n', 2*DeltaX1[20]*Ynew1[20], ' +- ' , DX(20))

'''
#DY
'''

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
TWO = A_3
DTWO = 0 
for i in range (0,N):
	DTWO = DTWO + DY(i)
print('Area 2 = ', A_3, ' +- ', DTWO)

'''
#D<pT2>
'''
DpT2 = np.sqrt( (1 / TWO)**2 * DONE**2 + (ONE / TWO**2)**2 * DTWO**2 )
print('<pT2> =', PT23,' +- ',  DpT2)

'''
#DTinit
'''
DTinit = DpT2 / np.sqrt( 2* PT23 )
print('Tinit =', Tinit3,' +- ',  DTinit )

#-------------------------------------------------------------------------------------------WRITE TO TXT

f = open("ppK2FixedRESULTS.txt", "a")
f.write('3	' + str(q) + '+-' + str(Dq) + '	' +str(Temper) + '+-' + str(DT) + '	' +str(Tinit3) + '+-' + str(DTinit) + '	' +str(valFCN3) +'/'+str(NDF3) +'\n')
f.close()

#--------------------------------------------------------------------------------------------------4



'''
#DX
'''
pT = X4
DpT = DeltaX4

A = parFit4[0]
DA = parErr4[0]

Temper = parFit4[1]
DT = parErr4[1]

q = parFit4[2]
Dq = parErr4[2]

#print('\n\npT :', pT, '\n', 'A :', A, '\n','T :', Temper, '\n', 'q :', q, '\n') 
print('\n\nA :', A, '\n','T :', Temper, '\n', 'q :', q) 
print('DpT :', DeltaX4[0], '\n', 'Dq :', parErr4[2], '\n','DT :', parErr4[1], '\n', 'DA :',parErr4[0]) 

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
ONE = Anew4
N = nCHAN
DONE = 0
for i in range (0,N):
	DONE = DONE + DX(i)
print('Area 1 = ', Anew4, ' +- ', DONE)
#print('\n', 2*DeltaX1[20]*Ynew1[20], ' +- ' , DX(20))

'''
#DY
'''

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
TWO = A_4
DTWO = 0 
for i in range (0,N):
	DTWO = DTWO + DY(i)
print('Area 2 = ', A_4, ' +- ', DTWO)

'''
#D<pT2>
'''
DpT2 = np.sqrt( (1 / TWO)**2 * DONE**2 + (ONE / TWO**2)**2 * DTWO**2 )
print('<pT2> =', PT24,' +- ',  DpT2)

'''
#DTinit
'''
DTinit = DpT2 / np.sqrt( 2* PT24 )
print('Tinit =', Tinit4,' +- ',  DTinit )

#-------------------------------------------------------------------------------------------WRITE TO TXT

f = open("ppK2FixedRESULTS.txt", "a")
f.write('4	' + str(q) + '+-' + str(Dq) + '	' +str(Temper) + '+-' + str(DT) + '	' +str(Tinit4) + '+-' + str(DTinit) + '	' +str(valFCN4) +'/'+str(NDF4) +'\n')
f.close()



#---------------------------------------------------------------------------------------------------PLOT

'''
PLOT
'''
ROOT.gStyle.SetOptStat(0)
Plot1 = ROOT.TGraphErrors(nChan, x, y1, ex, ey1)
Plot1.SetMarkerStyle(20)
Plot1.SetMarkerColor(ROOT.kRed)
Plot1.SetMarkerSize(1.1)
Plot1.SetLineWidth(3)
Plot1.GetXaxis().SetTitle('p_{T} [GeV/c]')
Plot1.GetXaxis().SetTitleSize(0.05)
Plot1.GetXaxis().SetTitleOffset(0.85)

#Plot1.GetYaxis().SetTitle(' \\frac{\partial \sigma}{ \partial p_{T}} [\\frac{mb}{GeV/c}]')
Plot1.GetYaxis().SetTitle(' \\frac{\partial^{2} \sigma}{ \partial p_{T} \partial y} [\\frac{mb}{GeV/c}]')
Plot1.GetYaxis().SetTitleSize(0.05)
Plot1.GetYaxis().SetTitleOffset(0.85)



Plot1.SetTitle("K_{s}^{0} pp #sqrt{s_{NN}}= 5.02 TeV")
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
    





Plot2 = ROOT.TGraphErrors(nChan, x, y2, ex, ey2)
Plot2.SetMarkerStyle(21)
Plot2.SetMarkerColor(ROOT.kViolet-3)
Plot2.SetMarkerSize(1.1)
Plot2.SetLineWidth(3)

fFit2 = ROOT.TH1F('tsallis2','Data VS Tsallis', nCHAN - 1, X2 - dx2/2.)
fFit2.SetLineColor(ROOT.kViolet-3)
fFit2.SetLineWidth(2)
fFit2.SetLineStyle(10)

for chan in range(nCHAN):
    fFit2.SetBinContent(chan + 1 ,Y_2[chan])


Plot3 = ROOT.TGraphErrors(nChan, x, y3, ex, ey3)
Plot3.SetMarkerStyle(22)
Plot3.SetMarkerColor(ROOT.kBlue)
Plot3.SetMarkerSize(1.3)
Plot3.SetLineWidth(3)

fFit3 = ROOT.TH1F('tsallis3','Data VS Tsallis', nCHAN - 1, X3 - dx3/2.)
fFit3.SetLineColor(ROOT.kBlue)
fFit3.SetLineWidth(2)
fFit3.SetLineStyle(7)

for chan in range(nCHAN):
    fFit3.SetBinContent(chan + 1 ,Y_3[chan])



Plot4 = ROOT.TGraphErrors(nChan, x, y4, ex, ey4)
Plot4.SetMarkerStyle(29)
Plot4.SetMarkerColor(ROOT.kPink+8)
Plot4.SetMarkerSize(1.6)
Plot4.SetLineWidth(3)

fFit4 = ROOT.TH1F('tsallis4','Data VS Tsallis', nCHAN - 1, X4 - dx4/2.)
fFit4.SetLineColor(ROOT.kPink+8)
fFit4.SetLineWidth(2)
fFit4.SetLineStyle(3)



for chan in range(nCHAN):
    fFit4.SetBinContent(chan + 1 ,Y_4[chan])



Legend = ROOT.TLegend(0.49,0.64,0.87,0.87)
#text = '\chi^{2}/NDF = ' +str(valFCN1)+ '/' +str(NDF1)+ ',T_{init} = ' +str(Tinit1)+ ' GeV'

Legend.AddEntry(Plot1,'2.0 < y < 2.5, T_{init}= 0.704 GeV', 'ep')
Legend.AddEntry(Plot2,'2.5 < y < 3.0, T_{init}= 0.685 GeV', 'ep')
Legend.AddEntry(Plot3,'3.0 < y < 3.5, T_{init}= 0.671 GeV', 'ep')
Legend.AddEntry(Plot4,'3.5 < y < 4.0, T_{init}= 0.644 GeV', 'ep')

#Legend.SetFillColor(kWhite)
Legend.SetTextAlign(12)
Legend.SetTextSize(0.03)
Legend.SetTextFont(2)
Legend.SetFillStyle(0)

Legend1 = ROOT.TLegend(0.49,0.64,0.87,0.87)
Legend1.AddEntry(fFit1,' ', 'l')
Legend1.AddEntry(fFit2,' ', 'l')
Legend1.AddEntry(fFit3,' ', 'l')
Legend1.AddEntry(fFit4,' ', 'l')





Plot1.Draw("AP")

fFit1.Draw("SAME&l")
fFit2.Draw("SAME&l")
fFit3.Draw("SAME&l")
fFit4.Draw("SAME&l")

Plot2.Draw("SAME&P")
Plot3.Draw("SAME&P")
Plot4.Draw("SAME&P")


Legend1.Draw("SAME")
Legend.Draw("SAME")


ROOT.gPad.SetLogy(1)
ROOT.gPad.SetTicks(1,1)
ROOT.gPad.RedrawAxis()
time.sleep(120)
ROOT.gPad.Update()
