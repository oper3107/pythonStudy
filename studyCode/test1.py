import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.array([1.0, 2.0, 3.0])
print(x)

class student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def introduce(self):
        print("hi! my name is %s and I'm %d years old.", self.name, self.age)
    def goodbad(self):
        if(self.score > 70):
            print("yeah and I'm a pretty good student.")
        else:
            print("No actaully I'm not a good student.")


studentA = student("Jack", 36, 98)
studentA.introduce()
studentA.goodbad()

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

img=imread('lena.png')
plt.imshow(img)
plt.show