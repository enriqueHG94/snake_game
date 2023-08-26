import unittest
from food import Food


class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food()

    def test_refresh(self):
        x_before = self.food.xcor()
        y_before = self.food.ycor()
        self.food.refresh()
        x_after = self.food.xcor()
        y_after = self.food.ycor()
        self.assertNotEqual(x_before, x_after)
        self.assertNotEqual(y_before, y_after)


if __name__ == '__main__':
    unittest.main()
