from random import randint
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for divide in range(2, int(math.sqrt(number)) + 1):
        if number % divide == 0:
            return False
    return True


def run_game():
    random_element = randint(0, 100)
    question = random_element
    correct_answer = 'yes' if is_prime(random_element) else 'no'
    return (question, correct_answer)
