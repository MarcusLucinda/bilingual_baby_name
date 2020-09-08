'''
Search and get names from differents languages
'''
import csv
import requests
from bs4 import BeautifulSoup

# Spanish names


def spanish_m():
    rep = set()
    with open("./lists/source/spanish_male.csv") as f:
        reader = csv.reader(f)
        next(reader)
        with open("./lists/spanish_m.txt", 'w+') as t:
            for name in reader:
                first_name = name[0].split(" ")[0]
                if first_name not in rep:
                    t.write(f'{first_name}\n')
                    rep.add(first_name)


def spanish_f():
    rep = set()
    with open("./lists/source/spanish_female.csv") as f:
        reader = csv.reader(f)
        next(reader)
        with open("./lists/spanish_f.txt", 'w+') as t:
            for name in reader:
                first_name = name[0].split(" ")[0]
                if first_name not in rep:
                    t.write(f'{first_name}\n')
                    rep.add(first_name)


# Any other language

def name_indexer(language, gender):
    lang = language.lower()
    gen = gender.lower()
    start_url = (
        f'https://www.behindthename.com/names/gender/{gen}/usage/{lang}')
    names_site = requests.get(start_url).text
    soup_names = BeautifulSoup(names_site, 'lxml')
    next_page_url = ''
    page_limit = soup_names.find_all(
        'nav', {'class': 'pagination'})[-1] \
        .find("div", {'class': "pgblurb"}).text[-1]
    if page_limit.isnumeric():
        with open(f"./lists/{lang}_{gen[0]}.txt", 'w+', encoding='utf-8') as f:
            for num in range(2, (int(page_limit)+2)):
                for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')
                next_page_url = f'{start_url}/{num}'
                names_site = requests.get(next_page_url).text
                soup_names = BeautifulSoup(names_site, "lxml")
    else:
        with open(f"./lists/{lang}_{gen[0]}.txt", 'w+', encoding='utf-8') as f:
            for name in soup_names.find_all('span', {'class': 'listname'}):
                    f.write(f'{name.text.split(" ")[0]}\n')

if __name__ == "__main__":
    name_indexer('greek', 'feminine')
