"""
寻找水仙花数
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数阿姆斯特朗数（Armstrong number）。
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

Version 0.1
Author:FU, Chaojie
Date:2019.08.25
"""
for a in range(1,9):
    for b in range(0,9):
        for c in range(0,9):
            if a**3 + b**3 + c**3 == a*100+b*10+c:
                print(a*100 + b*10 +c)
