import random

RULE = 'Find the greatest common divisor of given numbers.'


def get_qcd(num1, num2):
    min_number = num1 if num1 < num2 else num2
    count = min_number
    while count > 0:
        if num1 % count == 0 and num2 % count == 0:
            return count
        else:
            count -= 1


def run_game():
    random_num1 = int(random.randrange(1, 10))
    random_num2 = int(random.randrange(1, 10))
    question = f'Question: {random_num1} {random_num2}'
    correct_answer = get_qcd(random_num1, random_num2)
    return (question, str(correct_answer))
