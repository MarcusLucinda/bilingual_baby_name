class Mixer:
    def __init__(self, lang1, lang2):
        self.lang1 = lang1
        self.lang2 = lang2

    def name_combiner(self):
        var = [self.lang1, self.lang2]
        sav = []
        for lang in var:
            names_list_lang = set()
            with open(f'.//lists/{lang}.txt', 'r', encoding='utf-8') as f:
                names = f.readlines()
                for name in names:
                    names_list_lang.add(name.replace("\n", ""))
                sav.append(names_list_lang)
        return sav[0] & sav[1]

if __name__ == '__main__':
    set_mix = Mixer('portuguese_f', 'romanian_f')
    print(sorted(set_mix.name_combiner()))
