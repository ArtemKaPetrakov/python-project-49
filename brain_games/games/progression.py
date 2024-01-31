from random import randint

RULE = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 100)
    step = randint(1, 10)
    stop = start + (step * 10)
    # Условие, чтобы поместились все значения с нужным рандомным шагом
    result = []

    for number in range(start, stop, step):
        result.append(str(number))
    return result


def run_game():
    progresion = generate_progression()
    random_element = randint(0, 9)
    # Выбираем рандомный элемент по индексу
    correct_answer = progresion[random_element]
    progresion[random_element] = '..'
    result = ' '.join(progresion)
    question = f'Question: {result}'
    return (question, correct_answer)
