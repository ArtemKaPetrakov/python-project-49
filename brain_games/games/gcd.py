import random

def run_game():
    rule = 'Find the greatest common divisor of given numbers.'

    random_number1 = int(random.randrange(1, 100))
    random_number2 = int(random.randrange(1, 100))
    question = f'Question: {random_number1} {random_number2}'

    min_number = random_number1 if random_number1 < random_number2 else random_number2
    count = min_number
    while count > 0:
        if random_number1 % count == 0 and random_number2 % count == 0:
            correct_answer = str(count)
            break
        else:
            count -= 1

    return (question, correct_answer, rule)