from brain_games.game_engine import game_run
from brain_games.games import even


# def even_game():
#     print('Welcome to the Brain Games!')
#     name = prompt.string('May I have your name? ').strip()
#     print(f'Hello, {name}!')
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#     count = 0
#     while count != 3:
#         random_number = random.randrange(0, 100)
#         print(random_number)
#         correct_answer = 'yes' if (random_number % 2 == 0) else 'no'
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
    # even_game()
    game_run(even)


if __name__ == '__main__':
    main()
