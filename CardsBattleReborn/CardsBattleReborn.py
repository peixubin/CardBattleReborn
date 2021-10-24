# -*- coding: UTF-8 -*-

import random
import sys
import os

import interpreter

try:
    sys_path = sys.argv[0]
    os.chdir(sys_path.replace("CardsBattleReborn.py", ""))
except:
    pass

print("-- -- -- 卡牌对决 -- -- --")
print("""规则：
1、双方初始血量：10000
2、对决之前，双方随机获得3张卡牌
3、每回合双方派出1张卡牌出战，对决后，出战卡牌消失，并重新抽取一张卡牌
4、敏捷高的一方进行反击，对方根据自身卡牌的防御力，扣除血量
5、接着敏捷低的一方进行反击，对方根据自身卡牌的防御力，扣除血量
6、血量低于0的一方输掉比赛
""")

# 血量
playerHP = 10000
enemyHP = 10000
# 卡池
cards = []
load = interpreter.Interpreter()
cards = load.interpreter(cards)

# 抽取卡牌
playerCards = []
enemyCards = []

# 展示卡牌函数
def show_card(card):
    for i in card:
        if "." not in i:
            print("{}:{}".format(i, card[i]), end=" ")
    print()
for i in range(5):
    a = random.randint(0, len(cards) - 1)
    playerCards.append(cards[a])
    b = random.randint(0, len(cards) - 1)
    enemyCards.append(cards[b])
while True:
    # 卡牌展示
    print("我方卡牌：")
    for i in playerCards:
        show_card(i)
    # 我方出牌
    try:
        playerSelect = input("派第几张卡牌出战：")
        playerC = playerCards[int(playerSelect) - 1]
        print("我方派出了：" + playerC["名称"])
    except IndexError:
        print("游戏内部错误(E00001)! 此错误可能是由你胡乱输入造成的,请慎重!")
        break
    # 敌方出牌
    enemySelect = random.randint(0, len(enemyCards) - 1)
    enemyC = enemyCards[enemySelect]
    print("敌方派出了：" + enemyC["名称"])

    # 我方先攻击
    if playerC["敏捷"] > enemyC["敏捷"]:
        print("我方发起攻击！")
        playerHurt = playerC["攻击力"] - enemyC["防御力"]
        if playerHurt < 0:
            playerHurt = 0
        enemyHP -= playerHurt
        # 技能
        if playerC[".技能"]:
            playerHP = playerC[".技能"](playerHP, playerC[".数值"])
        if enemyHP <= 0:
            print("对决结束，敌方血量为0，我方获胜！")
            break
        else:
            print("我方造成伤害：" + str(playerHurt) + "，敌方剩余血量：" + str(enemyHP))
        # 敌方反击
        if enemyC["攻击距离"] >= playerC["攻击距离"]:
            print("敌方发起反击！")
            enemyHurt = enemyC["攻击力"] - playerC["防御力"]
            if enemyHurt < 0:
                enemyHurt = 0
            playerHP = playerHP - enemyHurt
            # 技能
            if enemyC[".技能"]:
                enemyHP = enemyC[".技能"](enemyHP, enemyC[".数值"])
            if playerHP <= 0:
                print("对决结束，我方血量为0，敌方获胜！")
                break
            else:
                print("敌方造成伤害：" + str(enemyHurt) + "，我方剩余血量：" + str(playerHP))
    # 敌方先攻击
    elif playerC["敏捷"] < enemyC["敏捷"]:
        print("敌方发起攻击！")
        enemyHurt = enemyC["攻击力"] - playerC["防御力"]
        if enemyHurt < 0:
            enemyHurt = 0
        playerHP = playerHP - enemyHurt
        # 技能
        if enemyC[".技能"]:
            enemyHP = enemyC[".技能"](enemyHP, enemyC[".数值"])
        if playerHP <= 0:
            print("对决结束，我方血量为0，敌方获胜！")
            break
        else:
            print("敌方造成伤害：" + str(enemyHurt) + "，我方剩余血量：" + str(playerHP))
        # 我方反击
        if playerC["攻击距离"] >= enemyC["攻击距离"]:
            print("我方发起反击！")
            playerHurt = playerC["攻击力"] - enemyC["防御力"]
            if playerHurt < 0:
                playerHurt = 0
            enemyHP -= playerHurt
            # 技能
            if playerC[".技能"]:
                playerHP = playerC[".技能"](playerHP, playerC[".数值"])
            if enemyHP <= 0:
                print("对决结束，敌方血量为0，我方获胜！")
                break
            else:
                print("我方造成伤害：" + str(playerHurt) + "，敌方剩余血量：" + str(enemyHP))
    # 不攻击
    else:
        print("对方跑的太快， 追不上！")

    # 删除卡牌
    playerCards.remove(playerC)
    enemyCards.remove(enemyC)
    # 补充卡牌
    a = random.randint(0, len(cards) - 1)
    playerCards.append(cards[a])
    b = random.randint(0, len(cards) - 1)
    enemyCards.append(cards[b])

    # 魔法泉
    spring = random.randint(1, 100)
    if spring <= 30:
        print("魔法泉喷发！")
        if spring <= 15:
            print("攻击力低于 3000 的卡牌获得 泰坦祝福 ！")
            for i in cards:
                if i["攻击力"] < 3000:
                    i["buff"] = "泰坦祝福"
        else:
            print("攻击力高于 6000 的卡牌获得 混沌侵蚀 ！")
            for i in cards:
                if i["攻击力"] > 6000:
                    i["buff"] = "混沌侵蚀"
    else:
        print("魔法泉很安静……")

    # buff
    for i in cards:
        if "buff" in i:
            if i["buff"] == "泰坦祝福":
                i["攻击力"] += 1000
            elif i["buff"] == "混沌侵蚀":
                i["攻击力"] -= 1000
                if i["攻击力"] < 0:
                    i["攻击力"] = 0
