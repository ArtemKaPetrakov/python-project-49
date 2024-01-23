import random


def run_game():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_number = random.randrange(0, 100)
    question = f'Question: {random_number}'
    correct_answer = 'yes' if (random_number % 2 == 0) else 'no'

    return (question, correct_answer, rule)
