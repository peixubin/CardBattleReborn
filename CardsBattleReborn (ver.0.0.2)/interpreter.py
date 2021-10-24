# -*- coding: UTF-8 -*-
import skills

from skills import nonBuff

class Interpreter():
    def __init__(self):
        self.file = open("leagends.txt", "r")
        self.leagends = self.file.readlines()

    def interpreter(self, cards):
        for i in self.leagends:
            if "//" in i:
                continue
            self.base_leagend = i.split(" ")
            self.base_skill = self.base_leagend[5]
            if "health" == self.base_skill.split(":")[0]:
                self.skill_show = "使用此英雄时给己方召唤师增加{}血量".format(int(self.base_skill.split(":")[1]))
                self.skill_run = skills.health
                self.skill_num = int(self.base_skill.split(":")[1])
                self.skill_object = 1
            elif "damage" == self.base_skill.split(":")[0]:
                self.skill_show = "使用此英雄时减少敌方召唤师{}血量".format(int(self.base_skill.split(":")[1]))
                self.skill_run = skills.damage
                self.skill_num = int(self.base_skill.split(":")[1])
                self.skill_object = 2
            elif "health&damage" == self.base_skill.split(":")[0]:
                self.skill_show = "使用此英雄时减少敌方召唤师{}血量,并增加己方召唤师相同血量".format(int(self.base_skill.split(":")[1]))
                self.skill_run = skills.healthAndDamage
                self.skill_num = int(self.base_skill.split(":")[1])
                self.skill_object = 3
            elif "persent^damage" == self.base_skill.split(":")[0]:
                self.skill_show = "使用此英雄时额外减少敌方召唤师自身卡牌攻击力的{}倍的血量".format(float(self.base_skill.split(":")[1]))
                self.skill_run = skills.persentDamage
                self.skill_num = float(self.base_skill.split(":")[1])
                self.skill_object = 4
            elif "non^buff" == self.base_skill.split(":")[0]:
                self.skill_show = "使用此英雄时:若该英雄有buff属性,则将对敌召唤师造成攻击力乘以{}的伤害;反之,则将对敌召唤师造成攻击力除以{}的伤害".format(float(self.base_skill.split(":")[1]), float(self.base_skill.split(":")[1]))
                self.skill_run = nonBuff().nonBuff
                self.skill_num = float(self.base_skill.split(":")[1])
                self.skill_object = 5
            else:
                self.skill_show = "此英雄无技能"
                self.skill_run = False
                self.skill_object = 0
                self.skill_num = 0
            self.leagend = {"名称": self.base_leagend[0],
                            "攻击力": int(self.base_leagend[1]),
                            "防御力": int(self.base_leagend[2]),
                            "敏捷": int(self.base_leagend[3]),
                            "攻击距离": int(self.base_leagend[4]),
                            "技能": self.skill_show,
                            ".技能": self.skill_run,
                            ".技能代号": self.skill_object,
                            ".数值": self.skill_num}
            cards.append(self.leagend)
        return cards
