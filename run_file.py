from game_class import *

new_game = Game({'limit': 60, 'iter': 5}, [1, '1', '3', '4', '5', '6', '6'], {'string':  'hello',  'score': 0}, {'limit':  40,  'largest': 20})

print(new_game.fibonacci_limit())
print(new_game.fibonacci_iter())
print(new_game.prime_largest())
print(new_game.prime_limit())
print(new_game.scrabble_calc())
print(new_game.scrabble_calc())
print(new_game.remove_dupes())
print(new_game.get_chuck_joke())