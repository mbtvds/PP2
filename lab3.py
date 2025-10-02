import math
import random
from itertools import permutations

# 1. Class with getString and printString
class StringClass:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


# 2. Shape and Square
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# 3. Rectangle inheriting Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# 4. Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


# 5. Bank Account
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit accepted. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal accepted. New balance: {self.balance}")
        else:
            print("Funds Unavailable!")


# 6. Filter primes using lambda
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def filter_primes(lst):
    return list(filter(lambda x: is_prime(x), lst))


# Python function

# 1. Grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams


# 2. Fahrenheit to Celsius
def fahrenheit_to_celsius(F):
    return (5/9)*(F-32)


# 3. Chickens and Rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if chickens*2 + rabbits*4 == numlegs:
            return chickens, rabbits
    return None, None


# 4. filter_prime from list
def filter_prime(lst):
    return [x for x in lst if is_prime(x)]


# 5. Permutations of string
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


# 6. Reverse words in sentence
def reverse_sentence(s):
    return ' '.join(s.split()[::-1])


# 7. has_33
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False


# 8. spy_game
def spy_game(nums):
    code = [0,0,7]
    idx = 0
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == len(code):
                return True
    return False


# 9. Volume of sphere
def volume_sphere(r):
    return (4/3)*math.pi*r**3


# 10. Unique elements from list
def unique_list(lst):
    new = []
    for i in lst:
        if i not in new:
            new.append(i)
    return new


# 11. Palindrome check
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# 12. Histogram
def histogram(lst):
    for n in lst:
        print('*'*n)


# 13. Guess the number game
def guess_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1,20)
    guessesTaken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guessesTaken += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")
            break


# Python Function

# 1-5 Movies functions
def is_good_movie(movie):
    return movie["imdb"] > 5.5

def filter_good_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

def average_imdb(movies):
    return sum(m["imdb"] for m in movies)/len(movies)

def average_imdb_by_category(movies, category):
    filtered = [m for m in movies if m["category"]==category]
    return sum(m["imdb"] for m in filtered)/len(filtered)
