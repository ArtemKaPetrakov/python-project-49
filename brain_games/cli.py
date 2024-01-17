import prompt   # импорт библиотеки для общения с пользователем


def welcom_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
