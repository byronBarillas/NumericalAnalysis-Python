## SECANT METHOD. This progam will do n0 iterations of the secant method
#  method. This method is like the newton method but it does not need
#  the derivative of the function of interest.
#  Stopping criteria is iterations and toleratnce of the ERROR


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
p0 = float(raw_input('Initial Iterate p0: '))
p1 = float(raw_input('Initial Iterate p1: '))
tol= float(raw_input('Tolerance: '))

i = 1;
i2 = 1;
while i < n0:
    
    p = p0 - f(p0)*(p1 - p0)/(f(p1)-f(p0))
    
    if absolute(p0 - p) < tol:
        err = absolute(p0 - p)
        i = n0
    i = i + 1
    p0 = p1
    p1 = p
    print p0
    i2 = i2 + 1
print '''Secant method iterated %5d times to give %f
The approximation to the root with error %5f''' %(i2,p0,err)
    

