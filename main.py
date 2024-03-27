import os
import json
from time import sleep, localtime, strftime
import re
from string import Template
from getpass import getpass
from sys import platform
from pathlib import Path
from functions import (handle_keyboard_interrupt,
                       clear_terminal,
                       create_env_file,
                       check_env_variables,
                       # check_env_key,
                       update_env_variable,
                       write_env_variable,
                       check1,
                       check_requirements)
import settings


@handle_keyboard_interrupt
def main(pltf: str):
    # Импорт необходимых библиотек, после установки
    from simple_term_menu import TerminalMenu
    import paramiko
    import tqdm

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


def before_main():
    pltf = settings.pltf  # Платформа, на котором запущена программа
    env_file = settings.env_file  # .env - файл

    if not check_requirements("requirements.txt"):  # Установка необходимых библиотек, если они не установлены
        exit()

    sleep(0.5)
    clear_terminal(pltf=pltf)

    if not check1(env_file=env_file):  # Проверка на файл с переменными окружения
        exit()

    sleep(0.5)
    clear_terminal(pltf=pltf)

    # Импорт необходимых библиотек, после установки
    from colorama import init, Fore, Back, Style

    init(autoreset=True)  # Colorama

    sleep(1)
    main(pltf=pltf)


if __name__ == '__main__':
    before_main()
