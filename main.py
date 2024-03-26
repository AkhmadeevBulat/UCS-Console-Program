import os
import paramiko
import json
from time import sleep, localtime, strftime
from os import system
import re
from string import Template
from colorama import init, Fore, Back, Style
from getpass import getpass
from simple_term_menu import TerminalMenu
from sys import platform

from functions import handle_keyboard_interrupt, clear_terminal, find_file, create_env_file


@handle_keyboard_interrupt
def main(pltf: str):
    while True:  # Диалог с администратором
        clear_terminal(pltf)
        menu = ["Поиск устройства по ip/mac адресу",
                "Настройка зон",
                "Настройка интерфейса коммутатора",
                "",
                "Настройка программы",
                "",
                "Выход"]
        terminal_menu = TerminalMenu(menu, title="Выберете действие:", skip_empty_entries=True)
        menu_entry_index = terminal_menu.show()
        # print(f"Ты выбрал: {menu[menu_entry_index]}!")  # Получить имя выбранного
        # print(f"Ты выбрал: {terminal_menu.chosen_menu_index}!")  # Получить индекс выбранного

        match menu[menu_entry_index]:
            case "Поиск устройства по ip/mac адресу":
                pass
            case "Настройка зон":
                pass
            case "Настройка программы":
                while True:
                    menu_settings = ["Очистить log файл",
                                     "Изменить логин и пароль для подключения 'Сеть'",
                                     "Изменить логин и пароль для подключения 'Active Directory'",
                                     "Изменить логин и пароль для подключения 'Exchange'",
                                     "",
                                     "Назад"]
                    terminal_menu = TerminalMenu(menu_settings, title="Меню настроек:", skip_empty_entries=True)
                    menu_entry_index = terminal_menu.show()

                    match menu_settings[menu_entry_index]:
                        case "Очистить log файл":
                            pass
                        case "Изменить логин и пароль для подключения 'Сеть'":
                            pass
                        case "Изменить логин и пароль для подключения 'Active Directory'":
                            pass
                        case "Изменить логин и пароль для подключения 'Exchange'":
                            pass
                        case "Назад":
                            break
            case "Выход":
                break


def before_main(pltf: str):  # Проверка файлов, переменных и подключений к важным ресурсам

    # Проверка на файл с переменными окружения
    file_path = find_file(pltf)
    if file_path.exists():
        print("Файл ~/.env-ucs найден!")
    else:
        print("Файл ~/.env-ucs не найден!")
        create_env_file(pltf)
        print("Файл ~/.env-ucs создан!")

    # Проверка присутствие правильных переменных в файле


    sleep(2)
    main(pltf=pltf)


if __name__ == '__main__':
    init(autoreset=True)
    before_main(pltf=platform)
