# %% 2.1 Demical to Binary 
import math

def demical_to_binary(dem_num):
    dem_num = float(dem_num)
    dem_num_front = math.floor(dem_num)
    dem_num_rear  = dem_num - dem_num_front
    dem_num_rear_init = dem_num_rear
    bi_num_front = bin(dem_num_front).replace("0b","")
    bi_num_rear = []
    dem_num_rear_spl = ['2','2']

    while( dem_num_rear_spl[1] != '0'):
        dem_num_rear = dem_num_rear * 2
        dem_num_rear_spl = str(dem_num_rear).split(".")
        bi_num_rear.append(dem_num_rear_spl[0])
        dem_num_rear = float('0.'+dem_num_rear_spl[1])
        if len(bi_num_rear) >= 100:
            break
    
    bi_num_rear_len = len(bi_num_rear)
    bi_num_rear = ''.join(bi_num_rear)
    bi_num = float(bi_num_front) + float(bi_num_rear) / (10**bi_num_rear_len)
    if dem_num_rear_init == float(0.0):
        bi_num = int(bi_num)
    
    return bi_num

# 2.1.1
print('Binary :',demical_to_binary(input('Demical :')))
