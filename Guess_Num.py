# 這是一個猜數字的遊戲.
import random

guessesTaken = 0  # 猜測次數

print('嗨!你好! 請問你的英文簡稱是?')
myName = input()

number = random.randint(1, 20)  # 隨機產生1到20的數字，並命名為number
print('好的, ' + myName + ', 請在 1 - 20 中選定一個數字.')

for guessesTaken in range(6):  # 猜測6次，# range(6) = [0, 1, 2, 3, 4, 5]
    # print('請猜一個數字.') # 縮排4個半形空格
    # guess = input()  # 輸入猜測的數字
    # guess = int(guess)  # 將猜測的數字轉為整數
    guess = int(input('請猜一個數字.'))  # 將猜測的數字轉為整數

    if guess < number:  # 如果猜測的數字小於number
        print('這個數字 太小 了.') # Eight spaces in front of "print"

    if guess > number:
        print('這個數字 太大 了.')

    if guess == number:  # 如果猜測的數字等於number
        break

if guess == number: # 如果猜測的數字等於number
    #guessesTaken = str(guessesTaken + 1) #次數=陣列數+1
    guessesTaken = guessesTaken + 1
    if guessesTaken <= 3 :
        guessesTaken = str(guessesTaken) 
        print('超級無敵厲害, ' + myName + '! 你只用了 ' + guessesTaken + ' 次就猜對了!')
    else:
        guessesTaken = str(guessesTaken) + ' 次'
        print('厲害, ' + myName + '! 你用了 ' + guessesTaken + ' 次就猜對了!')

if guess != number: # 6次機會用完，如果猜測的數字不等於number
    number = str(number)
    print('不好意思. 正確答案的數字是 ' + number + '.')