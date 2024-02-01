import prompt

GAME_ROUNDS = 3


def game_run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').strip()
    print(f'Hello, {name}!')
    print(game.RULE)

    for _ in range(GAME_ROUNDS):
        question, correct_answer = game.generate_data_for_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ').strip()
        if (user_answer == correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
            # Перенос строки в f шаблоне
    else:
        print(f"Congratulations, {name}!")
