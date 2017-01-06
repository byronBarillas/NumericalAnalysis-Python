## Fixed point iteration. This progam will do n0 iterations of the fixed point
#  method. Stopping criteria is iterations and toleratnce of the ERROR.


#################################################################
################## IMPORTS ####################################
#################################################################


from math import *


#################################################################
################## FUNCTIONS ####################################
#################################################################

#Define the function of interest>>>>>>>>>>>>>>>>>>
gx = raw_input('Write the formula involving x: ')

formula = '''
def g(x):
    return %s
''' % gx

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

while i < n0:
    p = g(p0)
    
    if absolute(p0 - p) < tol:
        err = absolute(p0 - p)
        i = n0
    i = i + 1
    p0 = p
    print p0

print '''The fixed point iteration scheme iterated %5d times to give %5f
The approximation to the fixed point with error %5f''' %(i,p0,err)
    
