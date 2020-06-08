class human:
    name = "name"
    HP = 100
    MP = 100
    print("안녕하세요")

class player(human):
    AD = 70

    def att(self,enemy):
        if self.MP == 100:
            self.MP = 50
            enemy.HP = 50

class enemy(human):
    DP = 20

class npc(human):
    pass    


    