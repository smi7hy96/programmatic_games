import unittest
from game_class import *


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game({'limit': 60, 'iter': 5}, [1, '1', '3', '4', '5', '6', '6'], {'string':  'hello',  'score': 0}, {'limit':  40,  'largest': 20}, {'limit':  21,  'lower': 3, 'upper': 7})

    def test_fibonacci_limit(self):
        self.assertEqual(self.game.fibonacci_limit(), '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55')

    def test_fibonacci_iter(self):
        self.assertEqual(self.game.fibonacci_iter(), '0, 1, 1, 2, 3')

    def test_remove_dupes(self):
        self.assertEqual(self.game.remove_dupes(), '1, 3, 4, 5, 6')

    def test_scrabble_calc(self):
        self.assertEqual(self.game.scrabble_calc(), 'You scored 8 points! Total Score so far is 8 points!')
        self.game.scrabble_values['string'] = 'hey'
        self.assertEqual(self.game.scrabble_calc(), 'You scored 9 points! Total Score so far is 17 points!')

    def test_prime_limit(self):
        self.assertEqual(self.game.prime_limit(), '2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37')

    def test_prime_largest(self):
        self.assertEqual(self.game.prime_largest(), '19')

    def test_get_chuck_joke(self):
        self.assertIsInstance((self.game.get_chuck_joke()), str)

    def test_fizz_buzz(self):
        self.assertEqual(self.game.fizz_buzz(), '1, 2, fizz, 4, 5, fizz, buzz, 8, fizz, 10, 11, fizz, 13, buzz, fizz, 16, 17, fizz, 19, 20, fizzbuzz')
