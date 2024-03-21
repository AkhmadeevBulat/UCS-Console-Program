from sys import platform
from os import system
from time import sleep, localtime, strftime


def clear_terminal():  # Чистка терминала
    if platform == 'darwin' or platform == 'linux' or platform == 'linux2':
        system('clear')
    elif platform == 'win32':
        system('cls')


def time_moment():  # Возвращаю текущее время
    return strftime('%H:%M:%S', localtime())
