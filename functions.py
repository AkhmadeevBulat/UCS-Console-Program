from sys import platform
import os
from os import system
from time import sleep, localtime, strftime
import functools
from pathlib import Path
import subprocess


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


def create_env_file(env_file: str):
    with open(env_file, 'w') as file:
        file.write("")
    return True


def write_env_variable(env_file: str):
    with open(env_file, 'w') as file:
        file.write('# Файл с переменными для программы UCS-Console-Program.\n'
                   '# Разработчик: Ахмадеев Булат Наилевич\n\n'
                   'login_network=None\n'
                   'password_network=None\n'
                   'login_ad=None\n'
                   'password_ad=None\n'
                   'login_email=None\n'
                   'password_email=None\n')
    return True


def check_env_variables(pltf: str):
    if pltf == 'darwin':
        env_variables = dotenv_values(str(Path.home() / '.env-ucs'))
        required_variables = ['login_network',
                              'password_network',
                              'login_ad',
                              'password_ad',
                              'login_email',
                              'password_email']

        for variable in required_variables:
            if variable not in env_variables:
                return False
        return True


def update_env_variable(pltf: str, path: str, file_name: str, key: str, new_value: str):
    if pltf == 'darwin':
        env_file_path = str(Path.home() / '.env-ucs')  # Путь к файлу .env-ucs

        with open(env_file_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)  # Перемещаем указатель файла в начало
            for line in lines:
                if line.startswith(f"{key}="):
                    file.write(f"{key}={new_value}\n")
                else:
                    file.write(line)
            file.truncate()  # Обрезаем файл после записи

        print(f"Значение переменной {key} успешно обновлено в файле .env-ucs.")
        return True


def check1(env_file: str):  # Проверка на файл с переменными окружения
    if Path(env_file).exists():
        print(f"Файл [{env_file}] найден!")
        return True
    else:
        print(f"Файл [{env_file}] не найден!")
        if create_env_file(env_file=env_file):
            print(f"Файл [{env_file}] создан!")
            if write_env_variable(env_file=env_file):
                print("Переменные созданы!")
                return True
            else:
                print("Переменные не созданы!")
                return False
        else:
            print(f"Не удалось создать файл [{env_file}]!")
            return False


def check_requirements(requirements_file):
    try:
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
        return True
    except subprocess.CalledProcessError:
        print("Ошибка при установке библиотек.")
        return False

