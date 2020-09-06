from tkinter import *
from tkinter import ttk
from name_mixer import Mixer

lang_list = [
    'Italian',
    'Portuguese',
    'Spanish',
    'French',
    'Romanian',
]

gen_list = [
    'Masculine',
    'Feminine',
]

root = Tk()

root.title('Mixed Baby Names')
root.geometry('500x430')


def show_names():
    a = (f'{lang_select_1.get().lower()}_{gen_select.get().lower()[0]}')
    b = (f'{lang_select_2.get().lower()}_{gen_select.get().lower()[0]}')
    set_mix = Mixer(a, b)
    names = (sorted(set_mix.name_combiner()))
    text.delete(1.0, END)
    text.insert(END, names)
    text.see(END)


lang_1_label = Label(root, text='Language 1')
lang_1_label.grid(column=2, row=1, pady=(20,5))

lang_2_label = Label(root, text='Language 2')
lang_2_label.grid(column=3, row=1, pady=(20,5), padx=(0,20))

gen_1_label = Label(root, text='Gender')
gen_1_label.grid(column=5, row=1, pady=(20,5))

lang_select_1 = ttk.Combobox(root, value=lang_list, width=12)
lang_select_1.current(0)
lang_select_1.grid(column=1, row=2, columnspan=2, padx=(80, 20))

lang_select_2 = ttk.Combobox(root, value=lang_list, width=12)
lang_select_2.current(0)
lang_select_2.grid(column=3, row=2, columnspan=2, padx=(0, 40))

gen_select = ttk.Combobox(root, value=gen_list, width=9)
gen_select.current(0)
gen_select.grid(column=5, row=2, columnspan=1,)

mix_button = Button(root, text="Get Mixed Names", command=show_names)
mix_button.grid(column=3, row=3, pady=30)

text = Text(root, wrap=WORD, width=60, height=15)
text.grid(column=1, columnspan=6, row=4, padx=(6,5))


root.mainloop()
