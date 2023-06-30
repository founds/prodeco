""" doc """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Fore, Back, Style
import datetime
import os
import sys
from includes.herbolarionavarro import herbolarionavarro

VERSION = "0.2"

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
        print(Fore.BLUE + "Iniciando Proceso de obtención de datos." + Fore.RESET)
        if not os.path.exists('Datasources'):
            os.mkdir('Datasources')

        DS = os.path.abspath(os.path.dirname(sys.argv[0])) + "/Datasources/"

        categories, subcategories, products = herbolarionavarro(DS).results()

        print(Fore.BLUE + "# Herbolario Navarro" + Fore.RESET)
        print(Fore.BLUE + "# Nº de Categorías total: " + Fore.RESET + Fore.GREEN + str(
            categories) + Fore.RESET)
        print(Fore.BLUE + "# Nº de Subcategorias total: " + Fore.RESET + Fore.GREEN + str(
            subcategories) + Fore.RESET)
        print(Fore.BLUE + "# Nº de productos total: " + Fore.RESET + Fore.GREEN + str(
            products) + Fore.RESET)


Prodeco()