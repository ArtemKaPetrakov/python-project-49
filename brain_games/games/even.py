from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    random_number = randint(0, 100)
    question = f'Question: {random_number}'
    correct_answer = 'yes' if (random_number % 2 == 0) else 'no'

    return (question, correct_answer)
