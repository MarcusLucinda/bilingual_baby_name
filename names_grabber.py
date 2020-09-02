'''
Search and get names from differents languages
'''
import csv
import requests
from bs4 import BeautifulSoup

# Spanish names


class Spanish:

    def spanish_m():
        rep = set()
        with open(".//lists/source/spanish_male.csv") as f:
            reader = csv.reader(f)
            next(reader)
            with open(".//lists/spanish_m.txt", 'w+') as t:
                for name in reader:
                    first_name = name[0].split(" ")[0]
                    if first_name not in rep:
                        t.write(f'{first_name}\n')
                        rep.add(first_name)

    def spanish_f():
        rep = set()
        with open(".//lists/source/spanish_female.csv") as f:
            reader = csv.reader(f)
            next(reader)
            with open(".//lists/spanish_f.txt", 'w+') as t:
                for name in reader:
                    first_name = name[0].split(" ")[0]
                    if first_name not in rep:
                        t.write(f'{first_name}\n')
                        rep.add(first_name)


# Portuguese names
class Portuguese:

    def portuguese_m():
        start_url = (
            'https://www.behindthename.com/names/gender/masculine/usage/portuguese')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/portuguese_m.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")

    def portuguese_f():
        start_url = (
            'https://www.behindthename.com/names/gender/feminine/usage/portuguese')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/portuguese_f.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")


# French names
class French:

    def french_m():
        start_url = (
            'https://www.behindthename.com/names/gender/masculine/usage/french')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/french_m.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")

    def french_f():
        start_url = (
            'https://www.behindthename.com/names/gender/feminine/usage/french')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/french_f.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")


# Italian names
class Italian:

    def italian_m():
        start_url = (
            'https://www.behindthename.com/names/gender/masculine/usage/italian')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/italian_m.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")

    def italian_f():
        start_url = (
            'https://www.behindthename.com/names/gender/feminine/usage/italian')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/italian_f.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")


# Romanian names
class Romanian:

    def romanian_m():
        start_url = (
            'https://www.behindthename.com/names/gender/masculine/usage/romanian')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/romanian_m.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")

    def romanian_f():
        start_url = (
            'https://www.behindthename.com/names/gender/feminine/usage/romanian')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        next_page_url = ''
        with open(".//lists/romanian_f.txt", 'w+', encoding='utf-8') as f:
            while next_page_url != start_url:
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_parcial = soup_names.find_all(
                    'nav', {'class': 'pagination'})[-1].find("a")['href']
                next_page_url = f'https://www.behindthename.com{next_parcial}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")


# Catalan names
class Catalan:

    def catalan_m():
        start_url = (
            'https://www.behindthename.com/names/gender/masculine/usage/catalan')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        with open(".//lists/catalan_m.txt", 'w+', encoding='utf-8') as f:
            for name in soup_names.find_all('span', {'class': 'listname'}):
                f.write(f'{name.text.split(" ")[0]}\n')

    def catalan_f():
        start_url = (
            'https://www.behindthename.com/names/gender/feminine/usage/catalan')
        names_site = requests.get(start_url).text
        soup_names = BeautifulSoup(names_site, 'lxml')
        with open(".//lists/catalan_f.txt", 'w+', encoding='utf-8') as f:
            for name in soup_names.find_all('span', {'class': 'listname'}):
                f.write(f'{name.text.split(" ")[0]}\n')
