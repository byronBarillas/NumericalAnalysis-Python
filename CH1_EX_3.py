## Determines the taylor polynomial about x = 0 of f(x) = cos(x)

#################################################################
################## IMPORTS ####################################
#################################################################


from math import cos,sin

#################################################################
################## FUNCTIONS ####################################
#################################################################


## Defines the function factorial
def factorial(c):
    factc = 1
    for c in range(1,c+1):
        factc = factc * c
    return factc

## Defines the function absolute value
def absolute(x):
    
    if x >= 0:
        x1 = x
    else:
        x1 = -1*x
    return x1
    
#################################################################
################## Body of module  ##############################
#################################################################

n = eval(raw_input('Number of terms = '))
x = float(raw_input('x =  '))
x0 = float(eval(raw_input('about x0 = ')))
COS = cos(x0)
SIN = sin(x0)

fdash = [COS]
s = -1          ## used in 1st loop
p = 0           ## used in 2nd loop

# 1st loop to create a list fdash to hold appropriate derivatives of series
for i in range(1,n):
    fdash = fdash + [(s)*SIN,(s)*COS]
    s = s * -1

# 2nd loop to add up the terms in the polynomial
for i in range(0,n):
    p = p + (fdash[i])*(x-x0)**i/(factorial(i))

# Compute the error in the approximation
error = absolute(p-cos(x))/absolute(p)

# Output the results
print ''' The taylor polynomial of cos(x) with %4d
terms gives %5f , and the relative error is %5f''' %(n,p,error)  





