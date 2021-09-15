#!/usr/bin/env python 3
import random
from datetime import datetime as dt
from typing import Any, Union
from builtins import input

try:
    import coloroma
except ImportError:
    import os
    print ("colorama isn\'t installed, installing now...")
    os.system('python -m pip install --user colorama')
    print ('colorama has been installed, restart Stith.')

from colorama import init
from colorama import Fore, Style

print('''                                                                               

                                    |                                                           
                                    |                                                           
                                ___-/_\-___                                                      
                    _____________/( . )\_____________                                           
                    *    |    |  (  \_/  )  |    |    *                                          
                        *|*  *|*  \_-+-_/  *|*  *|*                                              

                    ~ Script By: @Stevemats ~
''')

def main():
    print('\n1. Get A New Password')
    print('2. Exit')
    while True:
        try:
            choice = int(input('Enter choice: '))
            if choice == 1:
                pass_gen()
                break
            elif choice == 2:
                print("\n", "GoodBye!")
                break
            else:
                print("Invalid choice. Enter a choice in menu. 1 or 2")
                main()
        except ValueError:
            print("Invalid choice. Enter 1 or 2")
    exit()


def pass_gen():

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

    dean = "Your new password is: "
    now = dt.now() #get current time of PS change
    new = now.strftime("%m/%d/%Y, %H:%M:%S") 

    print("\n", dean + Fore.GREEN + password + f)
    print ("Password changed at: {} ".format(new))
    print(f + Style.BRIGHT + Fore.BLUE + '~~ Keep on changing your passwords on a timely based to keep off Intruders! ~~',
        "\t")

if __name__ == '__main__':
    main()