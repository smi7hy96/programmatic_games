import requests

class Game:
    def __init__(self, fib_numbers=None, dup_array=None, scrabble_values=None, prime_numbers=None, fizz_numbers=None, chuck_joke = None):
        if fib_numbers is None:
            fib_numbers = {'limit': None, 'iter': None}
        self.fib_numbers = fib_numbers
        if dup_array is None:
            dup_array = []
        self.dup_array = dup_array
        if fizz_numbers is None:
            fizz_numbers = {'limit': None, 'lower': None, 'upper': None}
        self.fizz_numbers = fizz_numbers
        if scrabble_values is None:
            scrabble_values = {'string': None, 'score': 0}
        self.scrabble_values = scrabble_values
        if prime_numbers is None:
            prime_numbers = {'limit':  None, 'largest': None}
        self.prime_numbers = prime_numbers
        self.chuck_joke= chuck_joke

    def fibonacci_limit(self):
        fib_list = ['0', '1']
        target_no = self.fib_numbers['limit']
        while target_no > int(fib_list[-1]):
            x = int(fib_list[-2])
            y = int(fib_list[-1])
            z = x + y
            if z < target_no:
                fib_list.append(str(z))
            else:
                break
        return ', '.join(fib_list)

    def fibonacci_iter(self):
        fib_list = ['0', '1']
        for i in range(self.fib_numbers['iter']-2):
            x = int(fib_list[-2])
            y = int(fib_list[-1])
            z = x + y
            fib_list.append(str(z))
        return ', '.join(fib_list)

    def remove_dupes(self):
        unique_list = []
        for x in range(len(self.dup_array)):
            new_value = str(self.dup_array[x])
            if len(unique_list) == 0:
                unique_list.append(new_value)
            else:
                found = False
                for y in range(len(unique_list)):
                    if unique_list[y] == new_value:
                        found = True
                if not found:
                    unique_list.append(new_value)

        return ', '.join(unique_list)

    def scrabble_calc(self):
        score = 0
        for x in self.scrabble_values['string']:
            score += self.__scrabble_points(x.upper())
        self.scrabble_values['score'] += score

        return f"You scored {score} points! Total Score so far is {self.scrabble_values['score']} points!"

    def __scrabble_points(self, letter):
        if letter in 'AEIOULNSTR':
            return 1
        elif letter in 'DG':
            return 2
        elif letter in 'BCMP':
            return  3
        elif letter in 'FHVWY':
            return 4
        elif letter == 'K':
            return 5
        elif letter in 'JX':
            return 8
        else:
            return 10

    def prime_limit(self):
        prime_numbers = []
        for x in range(1, self.prime_numbers['limit']):
            if self.__test_prime(x):
                prime_numbers.append(str(x))
        return ', '.join(prime_numbers)

    def prime_largest(self):
        prime_found = False
        max_number = self.prime_numbers['largest']
        while not prime_found or max_number > 0:
            if self.__test_prime(max_number):
                prime_found = True
                break
            else:
                max_number -= 1
                break
        return str(max_number)

    def __test_prime(self, num):
        if num > 1:
            if num == 2:
                return True
            if not num & 1:
                return False
            for i in range(2, (num//2) + 1):
                if num % i == 0:
                    return False
                    break
            return True
        else:
            return False

    def get_chuck_joke(self):
        joke = requests.get('https://api.chucknorris.io/jokes/random')
        self.chuck_joke = joke.json()['value']
        return self.chuck_joke

    def fizz_buzz(self):
        result_list = []
        for x in range(1, int(self.fizz_numbers['limit'])+1):
            result_list.append(self.__get_fizz(x))
        return ', '.join(result_list)

    def __get_fizz(self, x):
        lower = self.fizz_numbers['lower']
        upper = self.fizz_numbers['upper']
        if x % lower == 0 and x % upper == 0:
            return 'fizzbuzz'
        elif x % lower == 0:
            return 'fizz'
        elif x % upper == 0:
            return 'buzz'
        else:
            return str(x)
