## NEWTONS METHOD. This progam will do n0 iterations of NEWTONS 
#  method. Stopping criteria is iterations and tolerance of the ERROR

#output: approximation to the fixed point

#################################################################
################## IMPORTS ####################################
#################################################################


from math import *


#################################################################
################## FUNCTIONS ####################################
#################################################################

#Define the function of interest>>>>>>>>>>>>>>>>>>
fx = raw_input('f(x): ')

formula = '''
def f(x):
    return %s
''' % fx

exec(formula)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---

#Define the derivative of interest>>>>>>>>>>>>>>>>>>
fdashx = raw_input('f\'(x): ')

formula = '''
def fdash(x):
    return %s
''' % fdashx

exec(formula)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---

## Defines the function absolute value >>>>>>>>>>>>>
def absolute(x):
    
    if x >= 0:
        x1 = x
    else:
        x1 = -1*x
    return x1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---

 
#################################################################
################## Body of module  ##############################
#################################################################



n0 = int(raw_input('Number Of Iterations: '))
p0 = float(raw_input('Initial Iterate: '))
tol= float(raw_input('Tolerance: '))

i = 1;
i2 = 1;
while i < n0:
    
    p = p0 - f(p0)/fdash(p0)
    
    if absolute(p0 - p) < tol:
        err = absolute(p0 - p)
        i = n0
    i = i + 1
    p0 = p
    print p0
    i2 = i2 + 1
print '''Newtons method iterated %5d times to give %f
The approximation to the fixed point with error %5f''' %(i2,p0,err)
    
