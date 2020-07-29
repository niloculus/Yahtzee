from Die import Die

class Yahtzee():
    def __init__(self):
        self.chosen = ()
        self.d1 = Die(6)
        self.d2 = Die(6)
        self.d3 = Die(6)
        self.d4 = Die(6)
        self.d5 = Die(6)
        self.cup_of_dice = [self.d1, self.d2, self.d3, self.d4, self.d5]
        self.choices = {"Yahtzee": False, "Chance": False}

    def score(self, numbers):
        a = numbers.count(numbers[0])
        if a == 5:
            return 50
        else:
            return numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]

    def roll(self):
        if len(self.chosen) == 0:
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice
        else:
            for v in self.chosen:
                self.cup_of_dice[v].active = False
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice

    def choose(self, choice):
        self.chosen = choice

    def newchoose(self, key, myroll):
        if myroll.count(myroll[0]) == 5:
            if self.choices[key] == True:
                return False
            else:
                self.choices[key] = True
                return True
        else:
            if self.choices[key] == False:
                return False
            else:
                return True

            if self.choices[key] == True:
                return False
            else:
                self.choices[key] = True
                return True
            else:
            return False


     def test_newchoose(self):
                self.game = Yahtzee()
                values = [1, 1, 1, 1, 1]
                self.assertFalse(self.game.newchoose("Yahtzee", [1, 2, 3, 4, 5]))
                self.assertTrue(self.game.newchoose("Yahtzee", values))
                self.assertFalse(self.game.newchoose("Yahtzee", values))
                self.assertTrue(self.game.newchoose("Chance", [1, 2, 3, 4, 5]))
                self.assertFalse(self.game.newchoose("Chance", [1, 2, 3, 4, 5]))