import random

#問3
def euclid(a,b): 
    
    while a % b != 0: # a%bが0になるまで繰り返す
        a, b = b, a%b
    
    return(b)

#問4
def prime(a, b):
   
    if euclid(a,b) == 1: # aとbの最大公約数が1
        return True
    
    return False

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

print(euclid(a, b)) # aとbの最大公約数

if prime(a,b):
    print("互いに素である")
else:
    print("互いに素でない") 

#エクストラ問題
pairs = [(random.randint(1,10000),random.randint(1,10000)) for _ in range(100000) ] # 10万組生成
count = sum(1 for a,b in pairs if prime(a,b)) # Trueは1であるからsum関数によってaとbが互いに素な組の数が求まる
print(count/100000) # 確率