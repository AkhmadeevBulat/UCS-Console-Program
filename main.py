import paramiko
import json
from time import sleep, localtime, strftime
from os import system
from sys import platform
import re
from string import Template
from colorama import init, Fore, Back, Style
from getpass import getpass
from simple_term_menu import TerminalMenu

from functions import handle_keyboard_interrupt, clear_terminal


@handle_keyboard_interrupt
def main():
    while True:  # Диалог с администратором
        clear_terminal()
        menu = ["Поиск устройства по ip/mac адресу", "Настройка зон", "", "Настройка программы"]
        terminal_menu = TerminalMenu(menu, title="Выберете действие:", skip_empty_entries=True)
        menu_entry_index = terminal_menu.show()
        print(f"Ты выбрал: {menu[menu_entry_index]}!")

        x = input()


def before_main():  # Проверка переменных и подключений к важным ресурсам
    main()
    pass


if __name__ == '__main__':
    init(autoreset=True)
    before_main()
