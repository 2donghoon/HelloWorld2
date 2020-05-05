print("hello")
a = "제 이름은 손창하입니다."
b = "제 전화번호는 '01067662333'입니다."
a = input("제 이름은 손창하입니다.")
b = input("제 전화번호는 '01067662333'입니다.")
c = "My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!."
d = c.split()
g = d[1].lower()
h = d[6].capitalize()
i = " ".join(c.split())
e = i.replace("!!!!!!","")
f = e.replace(":",",")
j = f.replace("naMe","name")
k = j.replace("my","My")
print(k)