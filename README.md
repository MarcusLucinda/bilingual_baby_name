# bilingual_baby_name
Simple application that shows names that are common in two languanges.

Made this to practice some web scrapping, file management and Tkinter interface.

This is totally inspired on Bemmu Sepponen's site https://mixedname.com
It is waaay better and have far more functionalities

## Scrapping

The names were collected from behindthename.com using the BeautifulSoup library. The function named "name_indexer" receive the language and gender of the desired names, then the script collect all names from the page, checking if there are multiples pages. The names are stored in a txt file.

```python
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
```

## Names combining

The class "Mixer" receive the two desired languages, then the function "name_combiner" will read the txt files, store the names in sets and return the ones that are common for both languages.

```python
def name_combiner(self):
        var = [self.lang1, self.lang2]
        sav = []
        for lang in var:
            names_list_lang = set()
            file_path = self.resource_path('lists/')
            with open(f'{file_path}{lang}.txt', 'r', encoding='utf-8') as f:
                names = f.readlines()
                for name in names:
                    names_list_lang.add(name.replace("\n", ""))
                sav.append(names_list_lang)
        return sav[0] & sav[1]
```

So, calling;
```python
mix = Mixer("portuguese_f", "russian_f")
print(mix.name_combiner())
```

Will result in
```
{'LENA', 'ISIDORA', 'OLGA', 'ALBINA', 'DIANA', 'EVA', 'ELVIRA', 'ALEX', 'MARTA', 'LARA', 'SABINA', 'DINA', 'ALEXANDRA', 'SOFIA', 'TATIANA', 'ANGELINA', 'MARIA', 'MARINA', 'VERA'}
```
