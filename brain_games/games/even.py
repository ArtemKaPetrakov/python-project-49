import random


def run_game():
    rule = 'Answer "yes" if number even otherwise answer "no".'
    question = random.randrange(0, 100)
    correct_answer = 'yes' if (question % 2 == 0) else 'no'

    return (question, correct_answer, rule)
