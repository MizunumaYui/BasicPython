epsilon = 1 #イプシロンを1とする

while 1 + epsilon > 1: #最小のイプシロンを求める 
    epsilon /= 2

print(epsilon * 2)