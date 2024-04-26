def judge_1(): # 入力した値の型の判定
   
    n = float(input("自然数nを入力:"))
   
    if n.is_integer() and n > 0: #nが自然数ならばnをint型にする
        return int(n)
   
    else: #実数や負の数ならばエラーを出す
        raise ValueError("自然数を入力してください")


def prime_number(n): # 素数判定
  
    if n < 2:
        return False

    else:
        for i in range(2, int(n**(1/2)+1)): #2以上√a以下(整数)で割り切れる値があるか調べる
            if n % i == 0:
                return False
                break
        return True        

n = judge_1()

prime = prime_number(n)

if prime:
    print("素数である")

else:
    print("素数でない")