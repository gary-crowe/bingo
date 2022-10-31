import random #Condernsed solo version with call and player together
import numpy as np

def genUSA():
    test1=np.array(random.sample(range(1,16),5))
    test2=np.array(random.sample(range(16,31),5))
    test3=np.array(random.sample(range(31,46),5))
    test4=np.array(random.sample(range(46,61),5))
    test5=np.array(random.sample(range(61,76),5))

    test= np.concatenate((test1,test2,test3,test4,test5))
    test= test.reshape(5,5)
    print(np.array2string(test, separator=','))

if __name__ == "__main__":
    genUSA()
