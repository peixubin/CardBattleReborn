# -*- coding: UTF-8 -*-

import random
import sys
import os

import interpreter
import player as p

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

# 卡池
cards = []
load = interpreter.Interpreter()
cards = load.interpreter(cards)

player = p.Player(cards)
enemy = p.Enemy(cards)

while True:
    player.learn_enemy(enemy)
    enemy.learn_enemy(player)
    # 展示我方卡牌
    player.show()
    # 出牌2
    try:
        player.out_card()
        enemy.out_card()
    except ValueError:
        print("内部错误(E00001):由于您胡乱输入引起")
        break
    # 我方先攻击
    if player.playerC["敏捷"] > enemy.enemyC["敏捷"]:
        print("我方发起攻击！")
        player.learn_enemy(enemy)
        if player.hit():
            break
        # 敌方反击
        if enemy.enemyC["攻击距离"] >= player.playerC["攻击距离"]:
            print("敌方发起反击！")
            enemy.learn_enemy(player)
            if enemy.hit():
                break
    # 敌方先攻击
    elif player.playerC["敏捷"] < enemy.enemyC["敏捷"]:
        print("敌方发起攻击！")
        enemy.learn_enemy(player)
        enemy.hit()
        # 我方反击
        if player.playerC["攻击距离"] >= enemy.enemyC["攻击距离"]:
            print("我方发起反击！")
            player.learn_enemy(enemy)
            if player.hit():
                break
    # 不攻击
    else:
        print("对方跑的太快， 追不上！")

    # 删除卡牌
    player.i_cards.remove(player.playerC)
    enemy.i_cards.remove(enemy.enemyC)
    
    # 补充卡牌
    player.get_card(cards)
    enemy.get_card(cards)

    # 魔法泉
    spring = random.randint(1, 200)
    if spring <= 51:
        print("魔法泉喷发！")
        if spring <= 15:
            print("攻击力低于 3000 的卡牌获得 泰坦祝福 ！攻击力每回合增加 1000 ！")
            for i in cards:
                if i["攻击力"] < 3000:
                    i["buff"] = "泰坦祝福"
        elif spring <= 30 and spring > 15:
            print("防御力低于 3000 的卡牌获得 神兽祝福 ！防御力增长 10% ！")
            for i in cards:
                if i["防御力"] < 3000:
                    i["buff"] = "神兽祝福"
        elif spring <= 45 and spring > 30:
            print("防御力大于 4000 的卡牌遭受 混沌轰击 ！防御力减少 10% ！")
            for i in cards:
                if i["防御力"] > 4000:
                    i["buff"] = "混沌轰击" 
        elif spring <= 50 and spring > 45:
            print("攻击力高于 6000 的卡牌遭受 混沌侵蚀 ！攻击力每回合减少 1000 ！")
            for i in cards:
                if i["攻击力"] > 6000:
                    i["buff"] = "混沌侵蚀"
        else:
            gone = random.choice(cards)
            ("神兽冲破云霄，掠走了{}...".format(gone["名称"]))
            cards.remove(gone)
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
            elif i["buff"] == "神兽祝福":
                i["防御力"] *= 1.1
                i["防御力"] = int(i["防御力"])
                del i["buff"]
            elif i["buff"] == "混沌轰击":
                i["防御力"] *= 0.9
                i["防御力"] = int(i["防御力"])
                del i["buff"]
