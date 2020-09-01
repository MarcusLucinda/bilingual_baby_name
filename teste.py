import csv

with open(".//lists/source/spanish_male.csv") as f:
    reader = csv.reader(f)
    with open(".//lists/spanish_m.txt", 'w+') as t:
        for coluna in reader:
            t.write(f'{coluna[0].split(" ")[0]}\n')
            #print(coluna[0].split(" ")[0])