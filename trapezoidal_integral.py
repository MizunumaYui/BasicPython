from math import sin
from math import pi


a = 0
b = pi / 2
N = 100 #分割数

h = (b - a) / N #一つの区間の幅
S_1 = 0 

for k in range(1, N + 1): #公式の総和の部分を求める
    S_1 += sin(a + (k - 1) * h) + sin(a + k * h)

S_2 = S_1 * h / 2 #全体の面積を求める

print(S_2)

