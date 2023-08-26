import unittest
from scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.update_scoreboard()
        self.assertEqual(self.scoreboard.score, 0)

    def test_game_over(self):
        self.scoreboard.game_over()
        self.assertEqual(self.scoreboard.score, 0)

    def test_increase_score(self):
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 1)


if __name__ == '__main__':
    unittest.main()
