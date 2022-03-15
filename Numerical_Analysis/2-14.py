# %% 2.14
import math
import numpy as np

def Taylor_Error_under(x, num_S, Round_num, Switch):
    Taylor = np.zeros((len(x),num_S))
    Error_abs = np.zeros((len(x),num_S))
    Error_rel = np.zeros((len(x),num_S))
    Needed_num = np.zeros(len(x))
    Taylor_Exp = 0
 
    for i in range(len(x)):
    
        for ii in range(num_S):
            Taylor[i,ii] = (x[i]-Round_num)**ii / math.factorial(ii)
            Taylor_Exp += Taylor[i,ii]
            Taylor[i,ii] = math.exp(Round_num) * Taylor_Exp
            Error_abs[i,ii] = abs(math.exp(x[i]) - Taylor[i,ii]) #Absolute Error
            Error_rel[i,ii] = 100 * abs(math.exp(x[i]) - Taylor[i,ii])/math.exp(x[i]) #Relative Error
            
            if Switch == 'On':
                if Error_rel[i,ii] <= 0.1:
                    Needed_num[i] = ii
                    print('X Value = %f\t |Num. of Terms = %d\t |Error = %f'%(x[i],Needed_num[i],Error_rel[i,ii]))
                    break
            elif Switch == 'Off':
                print('i={}\tii={},\tTaylor={},\tError(%)={}'.format(i,ii,Taylor[i,ii], Error_rel[i,ii]))

            
        Taylor_Exp = 0
    return Taylor
    
# (1)
x = [0.5]
num_S = 10 # Number of Series
Round_num = 0
Switch = 'mute'
Taylor = Taylor_Error_under(x,num_S,Round_num,Switch)
Taylor_ascend = np.sort(Taylor)
Taylor_descend = Taylor_ascend[:, ::-1]
Taylor_ascend = np.round(Taylor_ascend, 5)
Taylor_descend = np.round(Taylor_descend, 5)
Taylor_ascending, Taylor_descending = 0, 0
for k in range(Taylor.size):
    Taylor_ascending += Taylor_ascend[::,k]
    Taylor_descending += Taylor_descend[::,k]

Error_ascend_abs = abs(Taylor_ascending - round(math.exp(0.5),5))
Error_descend_abs = abs(Taylor_descending - round(math.exp(0.5),5))

Error_ascend_rel = abs(Taylor_ascending - round(math.exp(0.5),5)) / round(math.exp(0.5),5)
Error_descend_rel = abs(Taylor_descending - round(math.exp(0.5),5)) / round(math.exp(0.5),5)

print(Error_ascend_abs,Error_ascend_rel, Error_descend_abs, Error_descend_rel)