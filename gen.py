#!/usr/bin/env python 3.7
import random
from colorama import *
from typing import Any, Union
from builtins import input

print('''                                                                               

                                   |                                                           
                                   |                                                           
                              ___-/_\-___                                                      
                   _____________/( . )\_____________                                           
                  *    |    |  (  \_/  )  |    |    *                                          
                      *|*  *|*  \_-+-_/  *|*  *|*                                              


    ''')

init(autoreset=True)
f = "\n" * 1

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

try:
    length = int(input("Input a Length of your choice(e.g 5,34 ): "))
except NameError:
    assert isinstance(length, int) # native

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

print("\n")
dean = "Congrats! Your new password is:   "

print(dean + Fore.RED + password + f)
print(f + Style.BRIGHT + Fore.BLUE + '~~ Keep on changing your passwords on a timely based to keep off Intruders! ~~',
      "\t")
