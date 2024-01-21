#!/usr/bin/env python3
# import prompt
# import random


from brain_games.game_engine import game_run
from brain_games.games import calc


# def calc_game():
#     print('Welcome to the Brain Games!')
#     name = prompt.string('May I have your name? ').strip()
#     print(f'Hello, {name}!')
#     print('What is the result of the expression?')
#     count = 0
#     # operators = ['+', '-', '*']
#     while count != 3:
#         random_num1 = int(random.randrange(0, 11))
#         random_num2 = int(random.randrange(0, 11))
#         random_operator = operators[random.randrange(0, 3)]
#         print(f'Question: {random_num1} {random_operator} {random_num2}')
#         correct_answer = ''
#         match random_operator:
#             case '+':
#                 correct_answer = str(random_num1 + random_num2)
#             case '-':
#                 correct_answer = str(random_num1 - random_num2)
#             case '*':
#                 correct_answer = str(random_num1 * random_num2)
#             case _:
#                 print('Error')
#         user_answer = prompt.string('').strip()
#         # Обрезаю пробелы, если пользователь ошибился
#         if (user_answer == correct_answer):
#             count += 1
#             print('Correct!')
#         elif (user_answer != correct_answer):
#             print(f"'{user_answer}' is wrong answer ;(. "
#                   f"Correct answer was '{correct_answer}'")
#             # Перенос строки в f шаблоне
#     print(f"Congratulations, {name}!")

def main():
    game_run(calc)


if __name__ == '__main__':
    main()
