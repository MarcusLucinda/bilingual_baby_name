import os
import sys

class Mixer:
    def __init__(self, lang1, lang2):
        self.lang1 = lang1
        self.lang2 = lang2

    def resource_path(self, relative_path):
        self.relative_path = relative_path
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, self.relative_path)

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

