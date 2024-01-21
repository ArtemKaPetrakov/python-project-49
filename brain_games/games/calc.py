import random

def run_game():
    rule = 'What is the result of the expression?'
    operators = ['+', '-', '*']
    random_number1 = int(random.randrange(0, 11))
    random_number2 = int(random.randrange(0, 11))
    random_operator = operators[random.randrange(0, 3)]
    question = f'Question: {random_number1} {random_operator} {random_number2}'

    correct_answer = ''

    match random_operator:
            case '+':
                correct_answer = str(random_number1 + random_number2)
            case '-':
                correct_answer = str(random_number1 - random_number2)
            case '*':
                correct_answer = str(random_number1 * random_number2)
            case _:
                print('Error')

    return (question, correct_answer, rule)