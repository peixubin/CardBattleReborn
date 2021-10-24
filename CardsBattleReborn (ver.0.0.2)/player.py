import random

class Usr:
    def __init__(self, cards):
        self.health = 10000
        self.i_cards = []
        for i in range(5):
            self.get_card(cards)
    
    def learn_enemy(self, enemy):
        self.enemy = enemy
    
    def get_card(self, cards):
        a = random.randint(0, len(cards) - 1)
        self.i_cards.append(cards[a])
        

class Player(Usr):
    def show(self):
        # 卡牌展示
        print("我方卡牌：")
        for i in self.i_cards:
            for j in i:
                if "." not in j:
                    print("{}:{}".format(j, i[j]), end=" ")
            print()
    
    def out_card(self):
        try:
            playerSelect = input("派第几张卡牌出战：")
            self.playerC = self.i_cards[int(playerSelect) - 1]
            print("我方派出了：" + self.playerC["名称"])
        except IndexError:
            print("游戏内部错误(E00001)! 此错误可能是由你胡乱输入造成的,请慎重!")
    
    def hit(self):
        playerHurt = self.playerC["攻击力"] - self.enemy.enemyC["防御力"]
        if playerHurt < 0:
            playerHurt = 0
        self.enemy.health -= playerHurt
        # 技能
        skill = self.playerC[".技能"]
        skill_num = self.playerC[".技能代号"]
        if skill:
            if skill_num == 1:
                self.health = self.playerC[".技能"](self.health, self.playerC[".数值"])
            elif skill_num == 2:
                self.enemy.health = self.playerC[".技能"](self.enemy.health, self.playerC[".数值"])
            elif skill_num == 3:
                self.health, self.enemy.health = self.playerC[".技能"](self.health, self.enemy.health, self.playerC[".数值"])
            elif skill_num == 4:
                self.enemy.health = int(self.playerC[".技能"](self.playerC[".数值"], self.playerC["攻击力"], self.enemy.health))
            elif skill_num == 5:
                self.enemy.health = int(self.playerC[".技能"](self.playerC, self.enemy.health))
        if self.enemy.health <= 0:
            print("我方造成伤害：" + str(playerHurt) + "，敌方剩余血量：0")
            print("对决结束，敌方血量为0，我方获胜！")
            return True
        else:
            print("我方造成伤害：" + str(playerHurt) + "，敌方剩余血量：" + str(self.enemy.health))

class Enemy(Usr):
    def out_card(self):
        enemySelect = random.randint(0, len(self.i_cards) - 1)
        self.enemyC = self.i_cards[enemySelect]
        print("敌方派出了：" + self.enemyC["名称"])

    def hit(self):
        self.before_health = self.enemy.health
        enemyHurt = self.enemyC["攻击力"] - self.enemy.playerC["防御力"]
        if enemyHurt < 0:
            enemyHurt = 0
        self.enemy.health = self.enemy.health - enemyHurt
        # 技能
        skill = self.enemyC[".技能"]
        skill_num = self.enemyC[".技能代号"]
        if skill:
            if skill_num == 1:
                self.health = self.enemyC[".技能"](self.health, self.enemyC[".数值"])
            elif skill_num == 2:
                self.enemy.health = self.enemyC[".技能"](self.enemy.health, self.enemyC[".数值"])
            elif skill_num == 3:
                self.health, self.enemy.health = self.enemyC[".技能"](self.health, self.enemy.health, self.enemyC[".数值"])
            elif skill_num == 4:
                self.enemy.health = int(self.enemyC[".技能"](self.enemyC[".数值"], self.enemyC["攻击力"], self.enemy.health))
            elif skill_num == 5:
                self.enemy.health = int(self.enemyC[".技能"](self.enemyC, self.enemy.health))
        if self.enemy.health <= 0:
            print("敌方造成伤害：" + str(enemyHurt) + "，我方剩余血量：0")
            print("对决结束，我方血量为0，敌方获胜！")
            return True
        else:
            print("敌方造成伤害：" + str(enemyHurt) + "，我方剩余血量：" + str(self.enemy.health))
