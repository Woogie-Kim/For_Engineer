## 2.12 

def Tayler_Error_under(x, num_S, Round_num, Switch):
    import math
    import numpy as np
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
    return 


# (1)
x = [0.1, 0.5, 1, 5, 10, 50]
num_S = 100 # Number of Series
Round_num = 0
Switch = 'mute'
Tayler_Error_under(x,num_S,Round_num,Switch)

# (2)
x = [-0.1, -0.5, -1, -5]
num_S = 100 # Number of Series
Round_num = 0
Switch = 'On'
Tayler_Error_under(x,num_S,Round_num,Switch)