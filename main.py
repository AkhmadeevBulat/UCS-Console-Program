import paramiko
import json
from time import sleep, localtime, strftime
from os import system
from sys import platform
import re
from string import Template
from colorama import init, Fore, Back, Style
from getpass import getpass


def main():
    # while True:  # Диалог с администратором
    #     pass
    print(123)


def before_main():  # Проверка переменных и подключений к важным ресурсам
    main()
    pass


if __name__ == '__main__':
    init(autoreset=True)
    before_main()
