1 class human: 
2     name = "name" 
3     HP = 100 
4     MP = 100 
5     print("안녕하세요") 
6 
 
7 class player(human): 
8     AD = 70 
9 
 
10     def att(self,enemy): 
11         if self.MP == 100: 
12             self.MP = 50 
13             enemy.HP = 50 
14 
 
15 class enemy(human): 
16     DP = 20 
17 
 
18 class npc(human): 
19     pass     
 