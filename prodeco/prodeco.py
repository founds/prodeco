""" doc """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Fore, Back, Style

VERSION = "0.1"

class Prodeco():
    def __init__(self):
        print(Fore.BLUE + "######################################################" + Fore.RESET)
        print(Fore.BLUE + "##                Prodeco Versión: " + str(VERSION) + "              ##" + Fore.RESET)
        print(Fore.BLUE + "##                     Altsys                       ##" + Fore.RESET)
        print(Fore.BLUE + "##  https://www.altsys.es            info@altsys.es ##" + Fore.RESET)
        print(Fore.BLUE + "######################################################" + Fore.RESET)


Prodeco()