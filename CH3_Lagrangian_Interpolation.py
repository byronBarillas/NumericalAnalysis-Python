## LAGRANGE POLYNOMIAL FUNCTION
print '''Module makes a Lagrangian interpolating polynomial from data
derived from an inputed function and interval. \n'''
####                 -IMPORT MODULES-

from math import *

####                -DEFINE FUNCTIONS


#Define the function of interest --->
fx = raw_input('f(x): ')

formula = '''
def f(x):
    return %s
''' % fx

exec(formula)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#Divides interval into N equal sub-intervals --->

def slicer(I,N):
    return [I[0] + float(i)*(I[1]- I[0])/N for i in range(N+1) ]

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Make Lagrangian : (Inrterval,f(x) values for the interval) ---> F(x)*L(x) for all

def LP(N):

    b1 = '(x - I[m])'
    b2 = '(I[k] - I[i])'
    L = []
    for n in range(N+1):
        B1 = ''
        B2 = ''
        mrange = range(N+1)
        del mrange[n]
        
        for m in mrange:

            B1 = B1 + b1.replace('m',str(m))
            B1 = B1.replace(')(',')*(')
            B1 = B1.replace('k',str(n))
            B2 = B2 + b2.replace('i',str(m))
            B2 = B2.replace(')(',')*(')
            B2 = B2.replace('k',str(n))
            L1 = '(' + B1 + ')/(' + B2 + ')'
        
        L.append(L1)


    return L
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


####                -BODY OF MODULE-


I = eval(raw_input('Interval of interest in list form:'))

N = eval(raw_input('Number of sub-intervals'))

I = slicer(I,N)

G = [f(i) for i in I]



L = LP(N)

print G
# Now we define the P lagrange polynomial as a function :

def p(x,L,G):
    p = []
    for l, g in zip(L,G):
        
        p.append(eval(l)*g)
    
    return sum(p)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

## At this point we need a graphing function to let us see the polynomial we make
print p(7.5,L,G)
