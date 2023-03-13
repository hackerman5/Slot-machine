import random

sekos = [[0, 1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]]
def sukimas():
    rezultatas = "";
    for seka in sekos:
        rezultatas += str(random.choice(seka))
    return rezultatas

cnt = 0

for i in range(1000000):
    dabartinisSukimas = sukimas()
    if dabartinisSukimas == "777" :
        cnt += 1
print(cnt)