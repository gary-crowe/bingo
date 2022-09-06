import numpy as np
import tabulate 
def gene():
    ticket =np.full(27,1).reshape(9,3)
    ticket[:4,:] *=0
    [np.random.shuffle(ticket[:,i]) for i in range(3)]
    for i in range(9):
        nums =np.arange(1+10*i,11+10*i)
        np.random.shuffle(nums)
        ticket[i,:] *= np.sort(nums[:3])
    print(tabulate.tabulate(ticket.T))

gene()
