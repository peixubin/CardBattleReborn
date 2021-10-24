def health(player_health, health):
    return player_health + health


def damage(player_health, health):
    return player_health - health

def healthAndDamage(player_health1, player_health2, health):
    return (player_health1 + health, player_health2 - health)

def persentDamage(c_persent, c_damage, health):
    return health - c_persent * c_damage

class nonBuff:
    def nonBuff(self, enemyC, health):
        try:
            self.enemyC["buff"] = self.enemyC["buff"]
            return self.buffed(enemyC["攻击力"], enemyC[".数值"], health)
        except:
            return self.unbuffed(enemyC["攻击力"], enemyC[".数值"], health)
    def unbuffed(self, c_damage, num, health):
        return health - c_damage * num
    def buffed(self, c_damage, num, health):
        return health - c_damage / num
