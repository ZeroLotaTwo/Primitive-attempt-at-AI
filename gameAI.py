import json
class AI():
    rewardAmt = 1
    risk = 3
    def __init__(self):
        self.brain = [0 for _ in range(20)]
        self.cardsDrawn = []
        self.winnings = [0]

    def drawCommand(self):
        return '1'
    
    def endTurnCommand(self):
        return '0'
    
    def drew21(self):
        if len(self.cardsDrawn) == 0:
            return
        else:
            self.brain[self.cardsDrawn[-1] - 1] -= self.rewardAmt + self.risk

    def drawCard(self, num: int):
        self.cardsDrawn.append(num)
        self.reward(num)
        if(self.brain[num - 1] > 0):
            return self.drawCommand()
        else:
            self.gameEnd(num)
            return self.endTurnCommand()

    def reward(self, num: int):
        if len(self.cardsDrawn) <= 1:
            return
        pastCard = self.cardsDrawn[-2]
        if num > pastCard:
            self.brain[pastCard - 1] += self.rewardAmt
        else:
            self.brain[pastCard - 1] -= self.rewardAmt + self.risk
    
    def gameEnd(self, num: int):
        if num > max(self.winnings):
            self.brain[num - 1] -= self.rewardAmt + self.risk
        else:
            self.brain[num - 1] += self.rewardAmt
        self.winnings.append(num)
        self.cardsDrawn.clear()

    def aiSave(self):
        with open("AIBRAIN.json", "w") as f:
            json.dump(self.brain,f)
    
    def aiLoad(self):
        with open("AIBRAIN.json", "r") as f:
            self.brain = json.load(f)
