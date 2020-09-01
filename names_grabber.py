'''
Search and get names from differents languages
'''
import csv


class spanish:

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


if __name__ == '__main__':
    spanish.spanish_f()
