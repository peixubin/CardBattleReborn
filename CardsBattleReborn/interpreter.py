# -*- coding: UTF-8 -*-
import skills

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
            if "health" in self.base_skill:
                self.skill_show = "使用此英雄时给自身增加{}血量".format(int(self.base_skill.split(":")[1]))
                self.skill_run = skills.health
                self.skill_num = int(self.base_skill.split(":")[1])
            else:
                self.skill_show = "此英雄无技能"
                self.skill_run = False
                self.skill_num = 0
            self.leagend = {"名称": self.base_leagend[0],
                            "攻击力": int(self.base_leagend[1]),
                            "防御力": int(self.base_leagend[2]),
                            "敏捷": int(self.base_leagend[3]),
                            "攻击距离": int(self.base_leagend[4]),
                            "技能": self.skill_show,
                            ".技能": self.skill_run,
                            ".数值": self.skill_num}
            cards.append(self.leagend)
        return cards
