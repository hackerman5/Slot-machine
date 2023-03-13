import random

class LosimuAutomatas:
    def __init__(self, sekos, laimejimas):
        self.seka = [[i for i in range(10)]] * sekos
        self.laimejimai = laimejimas

    def sukimas(self):
        sukimoRezultatas = ''
        for sekaa in self.seka:
            sukimoRezultatas += str(random.choice((sekaa)))
        return sukimoRezultatas

    def simuliacija(self, sukimuSkaicius, turimaSuma, statymas):
        self.sukimuSkaicius, self.turimaSuma, self.statymas = sukimuSkaicius, turimaSuma, statymas
        auksoPuodas = 0
        pradineSuma = turimaSuma
        ismoketa = 0
        laimingiSukimai = 0

        for i in range(self.sukimuSkaicius):
            turimaSuma+=statymas
            dabartinisSukimas = self.sukimas()
            pataikymas = [item for item in self.laimejimai.keys() if item in dabartinisSukimas]
            if pataikymas:
                daugiklis = self.laimejimai[max(pataikymas)]
                ismokejimas = statymas*daugiklis
                turimaSuma -= ismokejimas
                ismoketa += ismokejimas
                laimingiSukimai += 1
                if daugiklis == self.laimejimai[max(self.laimejimai.keys())]:
                    auksoPuodas += 1
        laimejimas = turimaSuma - pradineSuma
        if laimejimas > 0:
            laimejimas = f"${float(laimejimas):,.2f}"
            return f"{laimingiSukimai} laimejimai/ {sukimuSkaicius} sukimai. Laimejimas {laimejimas}"
        elif laimejimas < 0:
            laimejimas = f"{float(laimejimas):,.2f}"
            laimejimas = str(laimejimas).replace("-", "-$")
            return f"{laimingiSukimai} laimejimai/ {sukimuSkaicius} sukimai. Laimejimas {laimejimas}"
        else:
            return f"{laimingiSukimai} laimejimai/ {sukimuSkaicius} sukimai. Laimejimas 0"



losimas = LosimuAutomatas(3, {'700': 50})
#print(losimas.seka)
#print(losimas.laimejimai)
print(losimas.simuliacija(1000, 20000, 2))