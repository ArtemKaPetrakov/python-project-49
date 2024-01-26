import prompt


def game_run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').strip()
    print(f'Hello, {name}!')
    # question, correct_answer, rule = game.run_game()
    print(game.RULE)

    count = 0

    while count < 3:
        question, correct_answer = game.run_game()
        print(question)
        user_answer = prompt.string('Your answer: ').strip()
        if (user_answer != correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
            # Перенос строки в f шаблоне
        elif (user_answer == correct_answer):
            count += 1
            print('Correct!')
    print(f"Congratulations, {name}!")
