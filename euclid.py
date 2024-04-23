#a = int(input("a の値を入力: "))
#b = int(input("b の値を入力: "))

#(1)
a = 10
b = 20

while a % b != 0: #a=bq+rのrが0になるまで繰り返す
    r = a % b
    a = b
    b = r

print(b)

#(2)
a = 14
b = 91

while a % b != 0:
    r = a % b
    a = b
    b = r

print(b)

#(3)
a = 91
b = 14

while a % b != 0: 
    r = a % b
    a = b
    b = r

print(b)

