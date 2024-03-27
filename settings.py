from sys import platform
from pathlib import Path


""" Название .env файла,  котором будут хранятся все переменные для работы программы """
name_env_file = '.env-ucs'

""" Автоматическая установка платформы, на котором запущена программа """
pltf = platform


env_file = str(Path.home() / name_env_file)
