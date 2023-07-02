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
    print(Fore.RED + "[Developed by Exorcism]" + Style.RESET_ALL)
    print()
    print(Fore.LIGHTBLUE_EX + "1. Convert data from UTF-8 to Shift_JIS")
    print("2. Convert data from Shift_JIS to UTF-8")
    print("3. Quit the program" + Style.RESET_ALL)
    print()

def get_user_choice():
    choice = input("Choose an option (1-3): ")
    while choice not in ['1', '2', '3']:
        print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        choice = input("Choose an option (1-3): ")
    return choice

def get_user_input():
    print()
    return input("Enter the data to convert: ")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            clear_console()
            print(Fore.RED + "[Developed by Exorcism]" + Style.RESET_ALL)
            data = get_user_input()
            converted_data = convert_utf8_to_shift_jis(data)
            print(Fore.GREEN + "Conversion result: " + converted_data + Style.RESET_ALL)
        elif choice == '2':
            clear_console()
            print(Fore.RED + "[Developed by Exorcism]" + Style.RESET_ALL)
            data = get_user_input()
            converted_data = convert_shift_jis_to_utf8(data)
            print(Fore.GREEN + "Conversion result: " + converted_data + Style.RESET_ALL)
        else:
            print(Fore.RED + "Thank you for using the program. Goodbye!" + Style.RESET_ALL)
            sys.exit()

        user_option = input("Do you want to quit (q), go back to the main menu (m), or perform another conversion (a)? ")
        if user_option == 'q':
            print(Fore.RED + "Thank you for using the program. Goodbye!" + Style.RESET_ALL)
            sys.exit()
        elif user_option == 'm':
            continue
        elif user_option == 'a':
            continue
        else:
            print(Fore.RED + "Invalid option. The program will now exit." + Style.RESET_ALL)
            sys.exit()

if __name__ == "__main__":
    main()
