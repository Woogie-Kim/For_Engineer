# Taylor Series (x = 2)

import math
import numpy as np
x = [0.01, 1]
num_S = 100 # Number of Series
Round_num = int(2)

Taylor = np.zeros((len(x),num_S))
Error_abs = np.zeros((len(x),num_S))
Error_rel = np.zeros((len(x),num_S))
Taylor_Exp = 0

for i in range(len(x)):
    for ii in range(num_S):
        Taylor[i,ii] = (x[i]-Round_num)**ii / math.factorial(ii)
        Taylor_Exp += Taylor[i,ii]
        Taylor[i,ii] = math.exp(Round_num) * Taylor_Exp
        Error_abs[i,ii] = abs(math.exp(x[i]) - Taylor[i,ii]) #Absolute Error
        Error_rel[i,ii] = abs(math.exp(x[i]) - Taylor[i,ii])/math.exp(x[i]) #Relative Error
        print('i={}\tii={},\tTaylor={},\tError(%)={}'.format(i,ii,Taylor[i,ii], Error_rel[i,ii]))
        
    Taylor_Exp = 0

