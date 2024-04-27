from math import sin
from math import pi
from math import sqrt
from math import exp

def fun_1(x): # (2)の関数
    
     return 4 / (1 + x**2)


def fun_2(x): # (3)の関数
    
    return sqrt(pi) * exp(-x**2)


def integral(f, a=0, b=1, n=100): # 台形積分

    h = (b - a) / n
    S_1 = 0 

    for k in range(1, n + 1): #公式の総和の部分
        S_1 += f(a + (k - 1) * h) + f(a + k * h)

    return(S_1 * h / 2) #全体の面積


#(1)
print(integral(sin, 0, pi/2, 50))

#(2)
print(integral(fun_1, 0, 1, 100))

#(3)
print(integral(fun_2, -100, 100, 1000))


