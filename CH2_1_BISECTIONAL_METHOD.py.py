## Bisection Method.

## INPUT: This module takes in a function and an interval and the number of iterations
## OUTPUT: Function minimum in the interval and the x value associated

################################
#######   IMPORTS   ############
################################

from math import *


################################
#######DEFINE FUNCTIONS#########
################################

#Define the function of interest>>>>>>>>>>>>>>>>>>
fx = raw_input('Write the formula involving x: ')

formula = '''
def f(x):
    return %s
''' % fx

exec(formula)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---------


## Defines the function absolute value >>>>>>>>>>>
def absolute(x):
    
    if x >= 0:
        x1 = x
    else:
        x1 = -1*x
    return x1
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<----------




################################
#######Body of Module  #########
################################


# Input interval>>>>>>>>>>>>>>>>>>>>>
xint = raw_input('Interval of interest (in square brackets separated by a coma): ')
xint = eval(xint)
xint = [float(xint[0]),float(xint[1])]
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---


# Input number of iterations>>>>>>>>>>
N0 = raw_input('Number of Iterations: ')
N0 = int(N0)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---

# Evaluate function at endpoints >>>>>
fint = [f(xint[0]),f(xint[0])]
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---

# Main loop of function >>>>>>>>>>>>>>
i = 0;
while i < N0:
    p = xint[0] + (xint[1] - xint[0])/2
    Fp = f(p)

    if Fp*fint[0] >= 0:
        xint[0] = p
        fint[0] = Fp
    else:
        xint[1] = p
        fint[1] = Fp

    i = i + 1
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---


fmin = fint[0]
xmin = xint[0]

if fmin > absolute(fint[1]):
    xmin = xint[1]
    fmin = fint[1]
    

# Display results

print 'f = ', fmin,'at x = ', xmin, 'after',i,'iterations'

#####################
