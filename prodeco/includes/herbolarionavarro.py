""" doc """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from colorama import init, Fore, Back, Style
import pandas as pd
import datetime


class herbolarionavarro():
    def __init__(self):
        # Iniciar colorama
        init()

        #Variables
        # Lista de URLS y Titulos
        self.lstcategories = []
        self.lstsubcategories = []
        self.lstsubcategories2 = []
        self.lstproducts = []
        url_base = 'https://www.herbolarionavarro.es/'

        print(Fore.BLUE + "# Obteniendo datos: herbolarionavarro.es" + Fore.RESET)

        # Obtener categorias principales
        self.lstcategories.append(self.getCategories('https://www.herbolarionavarro.es/alimentacion-saludable'))

        numCategories = len(self.lstcategories[0])

        print(Fore.BLUE + "# Nº de categorias: " + Fore.RESET + Fore.GREEN + str(
            numCategories) + Fore.RESET)

        for item in self.lstcategories[0]:
            print(Fore.BLUE + "## Procesando: " + Fore.RESET + Fore.GREEN + item[1] + Fore.RESET)
            data = self.getCategories(url_base + item[1])
            if data is None:
                continue
            elif len(data) == 0:
                url = url_base + item[1]
                self.lstproducts.append(self.getProd(item[0], '', url))
            else:
                for subitem in data:
                    print(Fore.BLUE + "### Procesando: " + Fore.RESET + Fore.GREEN + subitem[0] + Fore.RESET)
                    urlsub = url_base + subitem[1]
                    self.lstproducts.append(self.getProd(item[0], subitem[0], urlsub))

        productsproc = []
        for i in self.lstproducts:
            if not i is None:
                for x in i:
                    productsproc.append(x)

        numproducts = len(productsproc)

        print(Fore.BLUE + "# Nº de productos total: " + Fore.RESET + Fore.GREEN + str(
            numproducts) + Fore.RESET)

        df = pd.DataFrame(productsproc)

        # Columnas de datos
        columns = ['categoria', 'subcategoria', 'nombre', 'marca', 'peso', 'precio', 'fecha']

        df.to_csv("herbolarionavarro.csv", sep=',', encoding='utf-8', header=columns)

    def getCategories(self, url):

        lstcategories = []
        page = None
        try:
            page = urlopen(url, timeout=10)
            soup_obj = BeautifulSoup(page, 'html.parser')

            # Obtener categorias
            sources = soup_obj.findAll('p', attrs={'class': 'max-w-6xl'})

            for num, source in enumerate(sources):
                if len(source) == 0:
                    continue
                elif len(source) >= 1:
                    categories = source.findAll('a', href=True)
                    for category in categories:
                        # Obtener URL y Titulo
                        lstcategories.append([category.text, category['href']])
                else:
                    print(Fore.RED + "No ha habido datos de categorias de los productos." + Fore.RESET)

            numCategories = len(lstcategories)
            print(Fore.BLUE + "- Nº de categorias encontradas: " + Fore.RESET + Fore.GREEN + str(
                numCategories) + Fore.RESET)

            return lstcategories
        except Exception as ex:
            print(Fore.RED + str(ex) + Fore.RESET)
        except HTTPError as error:
            print(error.status, error.reason)
        except URLError as error:
            print(error.reason)
        except TimeoutError:
            print(Fore.RED + "Request timed out" + Fore.RESET)
        finally:
            if page is not None:
                page.close()

    # Obtener productos
    def getProd(self, category, subcategory, url):
        page = None
        try:
            page = urlopen(url, timeout=10)
            soup_obj = BeautifulSoup(page, 'html.parser')
            products = soup_obj.findAll('div', attrs={'class': 'product-product-card'})

            lstproducts = []

            for product in products:
                title = product.find('span', attrs={'class': 'product-card-title'})
                brand = product.find('span', attrs={'class': 'product-label-additional'})
                size = product.find('span', attrs={'class': 'product-card-description'})
                price = product.find('span', attrs={'class': 'price'})
                datos = {
                    'categoria': category,
                    'subcategoria': subcategory,
                    'nombre': title.text.lstrip(),
                    'marca': brand.text,
                    'peso': size.text,
                    'precio': price.text.replace('\xa0€', ''),
                    'fecha': datetime.datetime.now().date()
                }

                lstproducts.append(datos)

            numproducts = len(lstproducts)
            print(Fore.BLUE + "- Nº de productos encontrados: " + Fore.RESET + Fore.GREEN + str(
                numproducts) + Fore.RESET)

            return lstproducts
        except Exception as ex:
            print(Fore.RED + str(ex) + Fore.RESET)
        except HTTPError as error:
            print(error.status, error.reason)
        except URLError as error:
            print(error.reason)
        except TimeoutError:
            print(Fore.RED + "Request timed out" + Fore.RESET)
        finally:
            if page is not None:
                page.close()

herbolarionavarro()