from sys import platform
from os import system
from time import sleep, localtime, strftime
import functools
from pathlib import Path
from dotenv import dotenv_values


def clear_terminal(pltf: str):  # Чистка терминала
    if pltf == 'darwin' or pltf == 'linux' or pltf == 'linux2':
        system('clear')
    elif pltf == 'win32':
        system('cls')


def time_moment():  # Возвращаю текущее время
    return strftime('%H:%M:%S', localtime())


def handle_keyboard_interrupt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print()

    return wrapper


def find_file(pltf: str):
    if pltf == 'darwin':
        home_dir = Path.home()  # Получаем путь к домашней директории пользователя
        file_path = home_dir / '.env-ucs'  # Формируем путь к файлу ~/.env-ucs.py
        return file_path


def create_env_file(pltf: str):
    if pltf == 'darwin':
        env_path = Path.home() / '.env-ucs'
        file_path = env_path / '.env-ucs'  # Формируем путь к файлу ~/.env-ucs.py
        with open(env_path, 'w') as file:
            file.write("")
        return file_path


def check_env_variables():
    env_variables = dotenv_values('~/.env-ucs')
    required_variables = ['login_network',
                          'password_network',
                          'login_ad',
                          'password_ad',
                          'login_email',
                          'password_email']
    missing_variables = []

    for variable in required_variables:
        if variable not in env_variables:
            missing_variables.append(variable)

    if len(missing_variables) == 0:
        print("Все переменные присутствуют в файле .env-ucs")
    else:
        print("Следующие переменные отсутствуют в файле .env-ucs:", missing_variables)
