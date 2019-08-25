"""
寻找完美数
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

Version 0.1
Author: FU, Chaojie
Date: 2019.08.25
"""
num = int(input('How many perfect numbers do you want to find:'))-int('0')
count = 0
number = 2
while count < num:
    check = 0
    for i in range(1,number-1):
        if number%i == 0:
            check += i
    if check == number:
        print(number)
        count += 1
    number += 1
