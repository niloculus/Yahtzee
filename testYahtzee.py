import unittest
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
        self.choices = {"Yahtzee": False, "Chance": False, "Large Straight": False, "Small Straight": False,
                        "Ones": False, "Twos": False, "Threes": False, "Fours": False, "Fives": False, "Sixes":False}

    def scores(self, numbers):
        d = {}
        if (self.choose("Yahtzee", numbers)):
            d["Yahtzee"]=50
            return d
        if (self.choose("Ones", numbers)):
            d["Ones"]=5
            return d
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

    def select(self, choice):
        self.chosen = choice

    def choose(self, key, myroll):
        if key == "Yahtzee":
            if myroll.count(myroll[0]) != 5:
                return False
        if myroll.count(myroll[0]) == 5:
            if self.choices[key] == True:
                return False
            else:
                self.choices[key] = True
                return True
        else:
            if self.choices[key] == True:
                return False
            else:
                self.choices[key] = True
                return True

class MyTestCase(unittest.TestCase):
    def test_yahtzee(self):
        self.game = Yahtzee()

    def test_roll(self):
        self.game = Yahtzee()
        values = self.game.roll()
        self.assertEqual(5, len(values))

    def test_die(self):
        d = Die(6)
        v = d.roll()
        self.assertGreater(v, 0)
        self.assertLess(v, 7)

    def test_select(self):
        self.game = Yahtzee()
        values = self.game.roll()
        print(values)
        self.game.select((0, 1))
        new_values = self.game.roll()
        print(new_values)
        self.assertEqual(values[0], new_values[0])
        self.assertEqual(values[1], new_values[1])

    def test_choose(self):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertFalse(self.game.choose("Yahtzee", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.choose("Yahtzee", values))
        self.assertFalse(self.game.choose("Yahtzee", values))
        self.assertTrue(self.game.choose("Chance", [1, 2, 3, 4, 5]))
        self.assertFalse(self.game.choose("Chance", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.choose("Large Straight",[1, 2, 3, 4, 5]))
        self.assertFalse(self.game.choose("Large Straight", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.choose("Small Straight", [1, 2, 3, 4, 5]))
        self.assertFalse(self.game.choose("Small Straight", [1, 2, 3, 4, 5]))
        # self.assertTrue(self.game.choose("Small Straight", [1, 2, 3, 4, 1]))
        # self.assertTrue(self.game.choose("Small Straight", [2, 3, 4, 5, 2]))
        # self.assertTrue(self.game.choose("Small Straight", [3, 4, 5, 6, 4]))
        # self.assertFalse(self.game.choose("Small Straight", [1, 2, 3, 4, 5]))


    def test_scores(self):
        self.game = Yahtzee()
        dict = self.game.scores([1,1,1,1,1])
        self.assertTrue(dict['Yahtzee'] == 50)
        self.assertTrue(dict["Ones"] == 5)
        self.assertTrue(dict["Twos"] == 0)
        self.assertTrue(dict["Threes"] == 0)
        self.assertTrue(dict["Fours"] == 0)
        self.assertTrue(dict["Fives"] == 0)
        self.assertTrue(dict["Sixes"] == 0)
        self.assertTrue(dict["Chance"] == 0)
        self.assertTrue(dict["Small Straight"] == 0)
        self.assertTrue(dict['Large Straight'] == 0)
        # self.game = Yahtzee()
        # values = [1, 1, 1, 1, 1]
        # self.assertTrue(self.game.score(values) == 50)
        # values = [1, 2, 3, 4, 5]
        # self.assertTrue(self.game.score(values) == 15)





if __name__ == '__main__':
    unittest.main()

# values = self.game.roll()
# if len(self.game.roll()):
#     values.append(values)
#     they_are_all_the_same = True
#     return 50
# else:
#     return sum(values)
# self.score = numbers
# values = self.game.roll()
