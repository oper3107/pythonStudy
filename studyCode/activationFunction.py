import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype=np.int64)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

#plt.plot(x,y)
#plt.ylim(-0.1, 1.1)
#plt.show()

def sigmoid(x):
        return 1/(1+np.exp(-x))
    

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

x = np.arange(-5.0, 5, 0.1)
y = sigmoid(x)
#plt.plot(x,y)
#plt.ylim(-0.1, 1.1)
#plt.show()

def relu(x):
    return np.maximum(0,x)

x = np.array([1,2])

w = np.array([[1,3,5], [2,4,6]])

y = np.dot(x,w)
print(y)
print(y)