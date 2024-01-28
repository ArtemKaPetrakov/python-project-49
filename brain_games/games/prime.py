import random
import math


def is_prime(number):
    if number < 2:
        return False
    # if number == 2 or number == 3:
    #     return True
    # if number % 2 == 0:
    #     return False
    for divide in range(2, int(math.sqrt(number)) + 1):
        if number % divide == 0:
            return False
    return True


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    # rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    random_element = random.randrange(0, 100)
    question = f'Question: {random_element}'
    correct_answer = 'yes' if is_prime(random_element) else 'no'
    return (question, correct_answer)
