## Numerical Analysis
# Seoul Univ. 
# Energy Resources Eng.
# Experience Practice 

x = [7.5, 0.75 ,0.075, 0.0075]
y_1 = []
y_2 = []
for i in range(4):
    y_1 = 3 + 12*x[i] - 8*(x[i])**2 + (x[i])**3 
    y_2 = 3 + x[i]*(12-x[i]*(8-x[i]))
    print(y_1,'\n',y_2)

print('=============END=============\n\n')


# %% Taylor Series (x = 2)
import math
import numpy as np
x = [0.01, 0.1, 1, 10]
num_S = 20 # Number of Series

Taylor = np.zeros((len(x),num_S))
Error_abs = np.zeros((len(x),num_S))
Error_rel = np.zeros((len(x),num_S))
Taylor_Exp = 0

for i in range(len(x)):
    for ii in range(num_S):
        Taylor[i,ii] = (x[i])**ii / math.factorial(ii)
        Taylor_Exp += Taylor[i,ii]
        Taylor[i,ii] = Taylor_Exp
        Error_abs[i,ii] = abs(math.exp(x[i]) - Taylor[i,ii]) #Absolute Error
        Error_rel[i,ii] = abs(math.exp(x[i]) - Taylor[i,ii])/math.exp(x[i]) #Relative Error
        print('i={}\tii={},\tTaylor={},\tError(%)={}'.format(i,ii,Taylor[i,ii], Error_rel[i,ii]))
        
    Taylor_Exp = 0

    

        
