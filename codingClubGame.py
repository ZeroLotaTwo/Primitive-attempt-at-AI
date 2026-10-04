from random import randint
from gameAI import AI
from time import sleep
ai = AI()
runs = 8000
class Game():
    def _getNum(self):
        return randint(1,21)

    def _intro(self):
        print("Welcome, you will draw a random number 1-21.")
        print("The number you draw will be how much money you recieve")
        print("But if you draw 21 you will lose.")
        print("But if you draw 10, you can either keep or draw again")
        print("You decide when you stop, but remeber if you draw 21 you lose")
        print("Good luck!!!\n")

    def _lose(self):
        print("You lost :(")
        self.rounds += 1
        self.eachWinning.append(0)
    
    def _endTurn(self):
        self.eachWinning.append(self.currMoney)
        self.rounds += 1

    def _getInput(self):
        return ai.drawCard(self.num)
    
    # def _redo(self, num: int):
    #     newNum = 10
    #     while(newNum == num):
    #         print(f"Would you like to redraw your {num}? 1 = y, 0 = N")
    #         redo = self._getInput()
    #         if redo == "1":
    #             newNum = self._getNum()
    #         else:
    #             break
    #     self.currMoney += newNum

    def __init__(self):
        self.rounds = 0
        self.currMoney = 0
        self.eachWinning = []
        self.num = 0
        # -1 is to end, 0 is to end round, 1 is to continue
        #self.controls = (-1, 0, 1)

    def _game(self):
        keepGoing = 1
        while keepGoing:
            self.num = self._getNum()
            print("You drew", self.num)
            if self.num == 21:
                self._lose()
                ai.drew21()
                break
            else:
                self.currMoney = self.num
            print(f"You will win ${self.currMoney}. Keep going? 1 = Y, 0 = n")
            choice = self._getInput()
            if choice == "0":
                self._endTurn()
                keepGoing = 0
            #sleep(1)
        
    def run(self):
        self._intro()
        contin = 1
        count = 0
        while contin:
            self._game()
            print(f"\nYou won {self.eachWinning[self.rounds - 1]} that round.")
            print("Do you wish to continue playing the game? 1 = y, 0 = N")
            count += 1
            if (0 and self._getInput() != "1") or count == runs:
                print(self.eachWinning)
                print("Cya next time!!!")
                contin = 0
            


test = Game()
# ai.aiLoad()
test.run()
ai
s = 0
for i in range(runs // 2):
    s += test.eachWinning[i]
print(s/(runs//2))
s = 0
for i in range(runs // 2, runs):
    s += test.eachWinning[i]
print(s/(runs//2))
print(ai.brain)
ai.aiSave()