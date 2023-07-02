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
    print(Fore.RED + "[開発者：エクソシズム]" + Style.RESET_ALL)
    print()
    print(Fore.LIGHTBLUE_EX + "1. UTF-8からShift_JISへのデータ変換")
    print("2. Shift_JISからUTF-8へのデータ変換")
    print("3. プログラムを終了する" + Style.RESET_ALL)
    print()

def get_user_choice():
    choice = input("オプションを選択してください（1-3）：")
    while choice not in ['1', '2', '3']:
        print(Fore.RED + "無効な選択です。もう一度お試しください。" + Style.RESET_ALL)
        choice = input("オプションを選択してください（1-3）：")
    return choice

def get_user_input():
    print()
    return input("変換するデータを入力してください：")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            clear_console()
            print(Fore.RED + "[開発者：エクソシズム]" + Style.RESET_ALL)
            data = get_user_input()
            converted_data = convert_utf8_to_shift_jis(data)
            print(Fore.GREEN + "変換結果：" + converted_data + Style.RESET_ALL)
        elif choice == '2':
            clear_console()
            print(Fore.RED + "[開発者：エクソシズム]" + Style.RESET_ALL)
            data = get_user_input()
            converted_data = convert_shift_jis_to_utf8(data)
            print(Fore.GREEN + "変換結果：" + converted_data + Style.RESET_ALL)
        else:
            print(Fore.RED + "プログラムをご利用いただきありがとうございました。さようなら！" + Style.RESET_ALL)
            sys.exit()

        user_option = input("終了する場合は（q）、メインメニューに戻る場合は（m）、他の変換を行う場合は（a）を入力してください：")
        if user_option == 'q':
            print(Fore.RED + "プログラムをご利用いただきありがとうございました。さようなら！" + Style.RESET_ALL)
            sys.exit()
        elif user_option == 'm':
            continue
        elif user_option == 'a':
            continue
        else:
            print(Fore.RED + "無効なオプションです。プログラムは終了します。" + Style.RESET_ALL)
            sys.exit()

if __name__ == "__main__":
    main()
