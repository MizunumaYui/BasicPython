#n = int(input("nの値を入力: ")) 

#(1)
n = 61 
prime = True #primeを用いてaが素数であると仮定する

if n < 2:
    print("素数でない")

else: #nが2以上の場合
    for i in range(2, int(n**(1/2)+1)): #2以上√a以下(整数)で割り切れる値があるか調べる
        if n % i == 0:
            prime = False
            break

    if prime: #True
        print("素数である")

    else: #False
        print("素数でない")  

#(2)
n = 10 
prime = True #primeを用いてaが素数であると仮定する

if n < 2:
    print("素数でない")

else: #nが2以上の場合
    for i in range(2, int(n**(1/2)+1)): #2以上√a以下(整数)で割り切れる値があるか調べる
        if n % i == 0:
            prime = False
            break

    if prime: #True
        print("素数である")

    else: #False
        print("素数でない")          