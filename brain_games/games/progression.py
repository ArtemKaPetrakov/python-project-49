from random import randint

RULE = 'What number is missing in the progression?'


def generate_progression():
    start = randint(1, 100)
    step = randint(1, 10)
    stop = start + (step * 10)
    # Условие, чтобы поместились все значения с нужным рандомным шагом
    result = list(range(start, stop, step))
    return result


def generate_data_for_round():
    progresion = generate_progression()
    random_element = randint(0, 9)
    # Выбираем рандомный элемент по индексу
    correct_answer = progresion[random_element]
    progresion[random_element] = '..'
    result = ' '.join([str(item) for item in progresion])
    question = result
    return (question, str(correct_answer))
