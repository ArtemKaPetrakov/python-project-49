from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data_for_round():
    random_number = randint(0, 100)
    question = random_number
    correct_answer = 'yes' if (random_number % 2 == 0) else 'no'

    return (question, correct_answer)
