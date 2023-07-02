import sys
import os
import colorama
from colorama import Fore, Style

colorama.init()

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def convert_utf8_to_shift_jis(data):
    return data.encode('utf-8').decode('shift-jis', 'ignore')

def convert_shift_jis_to_utf8(data):
    return data.encode('shift-jis').decode('utf-8', 'ignore')

def display_menu():
    clear_console()
    print(Fore.RED + "[Développé par Exorcism]" + Style.RESET_ALL)
    print()
    print(Fore.LIGHTBLUE_EX + "1. Convertir des données de UTF-8 vers Shift_JIS")
    print("2. Convertir des données de Shift_JIS vers UTF-8")
    print("3. Quitter le programme" + Style.RESET_ALL)
    print()

def get_user_choice():
    choice = input("Choisissez une option (1-3) : ")
    while choice not in ['1', '2', '3']:
        print(Fore.RED + "Choix invalide. Veuillez réessayer." + Style.RESET_ALL)
        choice = input("Choisissez une option (1-3) : ")
    return choice

def get_user_input():
    print()
    return input("Entrez les données à convertir : ")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            clear_console()
            print(Fore.RED + "[Développé par Exorcism]" + Style.RESET_ALL)
            data = get_user_input()
            converted_data = convert_utf8_to_shift_jis(data)
            print(Fore.GREEN + "Résultat de la conversion : " + converted_data + Style.RESET_ALL)
        elif choice == '2':
            clear_console()
            print(Fore.RED + "[Développé par Exorcism]" + Style.RESET_ALL)
            data = get_user_input()
            converted_data = convert_shift_jis_to_utf8(data)
            print(Fore.GREEN + "Résultat de la conversion : " + converted_data + Style.RESET_ALL)
        else:
            print(Fore.RED + "Merci d'avoir utilisé le programme. Au revoir !" + Style.RESET_ALL)
            sys.exit()

        user_option = input("Voulez-vous quitter (q), retourner au menu principal (m), ou effectuer une autre conversion (a) ? ")
        if user_option == 'q':
            print(Fore.RED + "Merci d'avoir utilisé le programme. Au revoir !" + Style.RESET_ALL)
            sys.exit()
        elif user_option == 'm':
            continue
        elif user_option == 'a':
            continue
        else:
            print(Fore.RED + "Option invalide. Le programme va maintenant se terminer." + Style.RESET_ALL)
            sys.exit()

if __name__ == "__main__":
    main()
