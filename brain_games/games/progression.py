import random

RULE = 'What number is missing in the progression?'


def generate_progression():
    start = int(random.randrange(1, 100))
    step = int(random.randrange(1, 10))
    stop = start + (step * 10)
    # Условие, чтобы поместились все значения с нужным рандомным шагом
    result = []

    for number in range(start, stop, step):
        result.append(str(number))
    return result


def run_game():
    # rule = 'What number is missing in the progression?'
    # progresion_length = 11
    # random_element = int(random.randrange(0, 1))
    # progresion_increment = int(random.randrange(1, 10))

    # star_number = int(random.randrange(1, 50))

    # for i in range(random_element, progresion_length, progresion_increment):
    #     result.append(i)
    # result = []
    # count = 0

    # while count < progresion_length:
    #     result.append(str(star_number))
    #     star_number += progresion_increment
    #     count += 1

    progresion = generate_progression()

    random_element = random.randrange(0, 9)
    # Выбираем рандомный элемент по индексу
    correct_answer = progresion[random_element]

    progresion[random_element] = '..'
    result = ' '.join(progresion)
    question = f'Question: {result}'

    return (question, correct_answer)
