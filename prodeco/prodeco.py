""" doc """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Fore, Back, Style
import datetime
from includes.herbolarionavarro import herbolarionavarro

VERSION = "0.1"

class Prodeco():
    def __init__(self):
        print(Fore.BLUE + "######################################################" + Fore.RESET)
        print(Fore.BLUE + "##                Prodeco Versión: " + str(VERSION) + "              ##" + Fore.RESET)
        print(Fore.BLUE + "##      Extraer productos y precios ecologicos de   ##" + Fore.RESET)
        print(Fore.BLUE + "##      diferentes paginas webs.                    ##" + Fore.RESET)
        print(Fore.BLUE + "##                     Altsys                       ##" + Fore.RESET)
        print(Fore.BLUE + "##  https://www.altsys.es            info@altsys.es ##" + Fore.RESET)
        print(Fore.BLUE + "######################################################" + Fore.RESET)
        print()
        print(Fore.BLUE + "######################################################" + Fore.RESET)
        herbolarionavarro()


Prodeco()