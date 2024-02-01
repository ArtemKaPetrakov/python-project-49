from random import randint

RULE = 'What is the result of the expression?'


def generate_data_for_round():
    operators = ['+', '-', '*']
    random_number1 = randint(0, 11)
    random_number2 = randint(0, 11)
    random_operator = operators[randint(0, 2)]
    question = f'{random_number1} {random_operator} {random_number2}'

    correct_answer = ''

    match random_operator:
        case '+':
            correct_answer = random_number1 + random_number2
        case '-':
            correct_answer = random_number1 - random_number2
        case '*':
            correct_answer = random_number1 * random_number2

    return (question, str(correct_answer))
