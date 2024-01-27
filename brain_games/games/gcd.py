import random

RULE = 'Find the greatest common divisor of given numbers.'


def get_qcd(num1, num2):
    min_number = num1 if num1 < num2 else num2
    count = min_number
    while count > 0:
        if num1 % count == 0 and num2 % count == 0:
            return str(count)
            # break
        else:
            count -= 1


def run_game():
    # rule = 'Find the greatest common divisor of given numbers.'

    random_num1 = int(random.randrange(1, 10))
    random_num2 = int(random.randrange(1, 10))
    question = f'Question: {random_num1} {random_num2}'
    correct_answer = get_qcd(random_num1, random_num2)

    # min_number = random_num1 if random_num1 < random_num2 else random_num2
    # count = min_number
    # while count > 0:
    #     if random_num1 % count == 0 and random_num2 % count == 0:
    #         correct_answer = str(count)
    #         break
    #     else:
    #         count -= 1

    return (question, correct_answer)
