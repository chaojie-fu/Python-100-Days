"""
Craps赌博游戏
玩家摇两颗色子
如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜
其他情况游戏继续玩家再次要色子
    如果摇出7点 庄家胜
    如果摇出第一次摇的点数 玩家胜
    否则游戏继续 玩家继续摇色子

玩家进入游戏时有1000元的赌注 全部输光游戏结束。

Version 0.1
Author: FU, Chaojie
Date: 2019.08.25
"""
from random import randint
print('You have 1000 yuan as you initial estate, now start.')
money = 1000
condition = input('Do you want to play the gambling?(Y/N): ')
while condition != 'Y' and condition != 'N':
    print('Wrong answer!')
    condition = input('Do you want to continue?(Y/N): ')
if condition == 'N':
    print('OK, see you then. You have 1000 yuan left.')

elif condition == 'Y':
    while condition == 'Y':
        gambling = int(input('How many money do you want to put on the table?: '))-int('0')
        if gambling > money:
            print('You can''t put money that don''t belong to you on the table!' )
            continue
        elif gambling <= 0:
            print('I regard that as a leaving request')
            break

        dice_1 = randint(1,6)
        dice_2 = randint(1,6)
        print('dice_1 = %d, dice_2 = %d' % (dice_1, dice_2))
        sum = dice_1 + dice_2
        if sum == 7 or sum == 11:
            money += gambling
            print('You win!')
        elif sum == 2 or sum == 3 or sum == 12:
            money -= gambling
            print('Opp, sorry that you lose.')
        else:
            print('Now that no one win or lose, I guess you need another toss.')
            dice_1 = randint(1,6)
            dice_2 = randint(1,6)
            print('dice_1 = %d, dice_2 = %d' % (dice_1, dice_2))
            sum_2 = dice_1 + dice_2
            if sum_2 == 7:
                money -= gambling
                print('Opp, sorry that you lose.')
            elif sum_2 == sum:
                money += gambling
                print('You win!')
            else:
                print('No one win or lose, game continues!')
                money += 0
        print('\n')
        print('You have %d yuan left' % money)
        print('-----------------------------------------------------------------')
        if money == 0:
            print('Sorry to notice you that you have broken up. See you next time!')
            break
        condition = input('Do you want to continue?(Y/N): ')
        while condition != 'Y' and condition != 'N':
            print('Invalid answer!')
            condition = input('Do you want to continue?(Y/N): ')
