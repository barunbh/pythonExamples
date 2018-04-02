import numpy as np
distance=[12,42,35,23,19,53,25,37,44]
time=[2,5,10,4,3,7,6,9,8]
np_dis=np.array(distance)
np_time=np.array(time)
speed=np_dis/np_time
print(speed)