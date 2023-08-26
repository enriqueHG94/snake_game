import unittest
from snake import Snake, STARTING_POSITIONS


class TestSnake(unittest.TestCase):

    def setUp(self):
        self.snake = Snake()

    def test_create_snake(self):
        self.assertEqual(len(self.snake.segments), 3)
        for i, segment in enumerate(self.snake.segments):
            self.assertEqual(segment.position(), STARTING_POSITIONS[i])

    def test_add_segment(self):
        self.snake.add_segment((100, 100))
        self.assertEqual(len(self.snake.segments), 4)
        self.assertEqual(self.snake.segments[-1].position(), (100, 100))

    def test_extend(self):
        last_position = self.snake.segments[-1].position()
        self.snake.extend()
        self.assertEqual(len(self.snake.segments), 4)
        self.assertEqual(self.snake.segments[-1].position(), last_position)


if __name__ == '__main__':
    unittest.main()
