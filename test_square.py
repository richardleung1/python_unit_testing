import unittest
import square

class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square.square(5), 25)
        self.assertEqual(square.square(10), 100)
        self.assertEqual(square.square(12), 144)
        self.assertEqual(square.square(15), 225)


if __name__ == '__main__':
    unittest.main()