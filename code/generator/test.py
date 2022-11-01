import random #Condernsed solo version with call and player together
import numpy as np

def genUSA():
    
    line1=(random.sample(range(1,16),5))
    line2=(random.sample(range(16,31),5))
    line3=(random.sample(range(31,46),5))
    line4=(random.sample(range(46,61),5))
    line5=(random.sample(range(61,76),5))

    card=np.stack((line1,line2,line3,line4,line5),axis=-1)
    return (np.array2string(card, separator=','))

if __name__ == "__main__":
    print (str(genUSA()))
