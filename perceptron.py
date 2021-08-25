import numpy as np
def AND(x1,x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if(tmp > theta):
        return 1
    else:
        return 0


print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))

x = np.array([0,1])
w = np.array([0.5, 0.5])
b = -0.7

r1 = np.sum(x*w)
print(r1)

r2 = np.sum(x*w) + b
print(r2)


def ANDB(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    ir = np.sum(x*w) + b
    if(ir > 0):
        return 1
    else:
        return 0


print(ANDB(0,0))
print(ANDB(1,0))
print(ANDB(0,1))
print(ANDB(1,1))

def NANDB(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    ir = np.sum(x*w)+b
    if(ir > 0):
        return 1
    else:
        return 0

print(NANDB(0,0))
print(NANDB(1,0))
print(NANDB(0,1))
print(NANDB(1,1))

def ORB(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    ir = np.sum(x*w) + b
    if(ir > 0):
        return 1
    else:
        return 0

print(ORB(0,0))
print(ORB(1,0))
print(ORB(0,1))
print(ORB(1,1))

def XORB(x1, x2):
    s1 = NANDB(x1,x2)
    s2 = ORB(x1, x2)
    y = ANDB(s1,s2)
    return y

print("XOR")
print(XORB(0,0))
print(XORB(1,0))
print(XORB(0,1))
print(XORB(1,1))