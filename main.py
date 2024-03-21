import paramiko
import json
from time import sleep, localtime, strftime
from os import system
from sys import platform
import re
from string import Template
from colorama import init, Fore, Back, Style
from getpass import getpass

from functions import handle_keyboard_interrupt, clear_terminal


@handle_keyboard_interrupt
def main():
    while True:  # Диалог с администратором
        clear_terminal()
        choiceMenu = input(Fore.GREEN + '|---------------------------------------------------------|\n'
                                        '| 1 - Поиск устройства по ip/mac адресу;                  |\n'
                                        '| 2 - Настройка зон;                                      |\n'
                                        '| 3 - ---;                                                |\n'
                                        '| 0 - Настройка программы.                                |\n'
                                        '|---------------------------------------------------------|\n'
                                        'Выберете действие: ')

        match choiceMenu:
            case '0':
                pass
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '9':
                pass
            case '10':
                pass


def before_main():  # Проверка переменных и подключений к важным ресурсам
    main()
    pass


if __name__ == '__main__':
    init(autoreset=True)
    before_main()
