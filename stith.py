#!/usr/bin/env python 3
import os
import random
import pyperclip
import urllib.request


from datetime import datetime as dt
from typing import Any, Union
from builtins import input

# Checking if the colorama module is installed. If not, it will install it.
try:
    from colorama import init
    from colorama import Fore, Style
except ImportError:
    import os
    print ("Installing missing required packages...")
    os.system('python -m pip install --user colorama')
    print ('colorama has been installed, restarting Stith...')


def main():

    print('''

                                        |
                                        |
                                    ___-/_\-___
                        _____________/( . )\_____________
                        *    |    |  (  \_/  )  |    |    *
                            *|*  *|*  \_-+-_/  *|*  *|*

                        ~ Script By: @Stevemats ~
    ''')

    print('\n1. Generate Password')
    print('2. Generate Passphrase')
    print('3. Exit')
    while True:
        try:
            choice = int(input('Enter choice: '))
            if choice == 1:
                pAsswords.pass_gen()
                break
            if choice == 2:
                pFrase.phrase_path()
                break
            elif choice == 3:
                print("\n", "GoodBye!")
                break
            else:
                print("Invalid choice. Enter a choice in menu. 1 or 2")
                main()
        except ValueError:
            print("Invalid choice. Enter 1 or 2")
    exit()

class pAsswords:

    def pass_gen():
        """
        It generates a random password.
        """

        init(autoreset=True)
        f = "\n" * 1

        symbol = 0
        lower = 0
        upper = 0
        number = 0
        count = 0
        password = []

        try:
            length = int(input("Input Password Length of your choice(e.g 12 ): "))
        except NameError:
            assert isinstance(length, int)

        while count < length:
            rand: Union[int, Any] = random.randint(0, 3)
            if rand == 0:
                lower += 1
                b = int(random.randint(97, 123))
                password.append(b)
            elif rand == 1:
                upper += 1
                b = random.randint(65, 91)
                password.append(b)
            elif rand == 2:
                number += 1
                b = random.randint(48, 58)
                password.append(b)
            elif rand == 3:
                r = random.randint(0, 2)
                symbol += 1
                if r == 0:
                    b = random.randint(33, 48)
                    password.append(b)
                elif r == 1:
                    b = random.randint(91, 97)
                    password.append(b)
                elif r == 2:
                    b = random.randint(123, 126)
                    password.append(b)
            count += 1
        password = "".join([chr(c) for c in password])
        pyperclip.copy(password)

        dean = "Your new password which has been autocopied to your clipboard is: "
        #get current time of PS change
        now = dt.now()
        new = now.strftime("%m/%d/%Y, %H:%M:%S")

        print("\n", dean + Fore.GREEN + password + f)
        print("Password length: ", "Containes a combination of ->",Fore.GREEN,len(password), "characters")
        print ("Password changed at: {} ".format(new))
        print(f + Style.BRIGHT + Fore.BLUE + '~~ Keep on changing your passwords on a timely based to keep off Intruders! ~~',
            "\t")


class pFrase:

    def phrase_path():
        """
        The function phrase_path() returns the path to the EFF wordlist seen in specified URL
        """
        URL = 'https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt'
        FILE_NAME = URL.split('/')[-1]
        THIS_DIR = os.path.dirname(os.path.realpath(__file__))
        WORDLIST = os.path.join(THIS_DIR, FILE_NAME)

        init(autoreset=True)
        f = "\n" * 1

        def download_wordlist():
            '''Download the EFF wordlist if not there already'''
            if not os.path.isfile(WORDLIST):
                print('creating a local wordlist db ...')
                urllib.request.urlretrieve(URL, WORDLIST)


        def get_words():
            '''Turn the EFF wordlist db file into a dict'''
            with open(WORDLIST, 'r') as i:
                lines = i.read().splitlines()
                phrase_dict = dict([x.split('\t') for x in lines])
            return phrase_dict


        def get_passphrase(phrase_dict):
            """
            This function takes a dictionary as an argument and returns a string.

            :param phrase_dict: A dictionary containing the passphrase
            """

            def get_dice_numbers():
                """
                It returns a list of random numbers between 1 and 6
                """
                num = ''
                for _ in range(0, 5):
                    num += str(random.randint(1, 6))
                return num

            # get a list of five 5-digit dice numbers
            word_list = [get_dice_numbers() for _ in range(0, 5)]
            # Returning a space-delimited string of the corresponding words from the EFF list.
            return ' '.join([phrase_dict[x] for x in word_list])
        download_wordlist()
        phrase_dict = get_words()
        new_passphrase = get_passphrase(phrase_dict)
        pyperclip.copy(new_passphrase)

        dean = "Your new passphrase which has been autocopied to your clipboard is: "
        # Getting the current time of the password change.
        now = dt.now()
        new = now.strftime("%m/%d/%Y, %H:%M:%S") 

        print("\n", dean + Fore.GREEN + new_passphrase + f)
        print("No.of characters in the passphrase: ", "Containes a combination of ->",
              Fore.GREEN, len(new_passphrase), "characters")
        print ("Passphrase generated at: {} ".format(new))
        print(f + Style.BRIGHT + Fore.BLUE + '~~ Keep on changing your passwords on a timely based to keep off Intruders! ~~',
              "\t")


if __name__ == '__main__':
    main()
