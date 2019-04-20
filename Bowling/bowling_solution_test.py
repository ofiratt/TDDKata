from bowling_solution import Bowling
from bowling_solution import ALL_BALLS_IN_FRAME
import unittest


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = Bowling()

    def rollMany(self, rolls, pins):
        for i in range(rolls):
            self.game.roll(pins)

    def rollSpare(self):
        self.game.roll(ALL_BALLS_IN_FRAME/2)
        self.game.roll(ALL_BALLS_IN_FRAME/2)

    def rollStrike(self):
        self.game.roll(ALL_BALLS_IN_FRAME)

    def test_zero_game(self):
        self.rollMany(20, 0)

        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.rollMany(20, 1)

        self.assertEqual(self.game.score(), 20)

    def test_spare(self):
        roll_after_spare = 3
        expected_score = ALL_BALLS_IN_FRAME + roll_after_spare*2

        self.rollSpare()
        self.game.roll(roll_after_spare)
        self.rollMany(17, 0)

        self.assertEqual(self.game.score(), expected_score)

    def test_strike(self):
        first_roll_after_strike = 4
        second_roll_after_strike = 3
        expected_score = ALL_BALLS_IN_FRAME + (first_roll_after_strike + second_roll_after_strike)*2

        self.rollStrike()
        self.game.roll(first_roll_after_strike)
        self.game.roll(second_roll_after_strike)
        self.rollMany(16, 0)
        self.assertEqual(self.game.score(), expected_score)

if __name__ == '__main__':
    unittest.main()
