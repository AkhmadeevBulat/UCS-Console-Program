import subprocess
import importlib.util


def check_requirements(requirements_file):
    try:
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
        print("Библиотеки успешно установлены.")
    except subprocess.CalledProcessError:
        print("Ошибка при установке библиотек.")


# Пример вызова функции для проверки наличия библиотек и их установки из requirements.txt
check_requirements("requirements.txt")
