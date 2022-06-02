import tkinter as tk
from tkinter import ttk
import system_convert


def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    k1 = value.find('+')
    k2 = value.find('-')
    k3 = value.find('*')
    k4 = value.find('/')
    k = max(k1, k2, k3, k4)
    s1 = system_convert.convert_n_to_10(value[:k], int(combo.get()))
    s2 = system_convert.convert_n_to_10(value[k+1:], int(combo1.get()))
    s3 = value[k]
    s0 = str(s1) + s3 + str(s2)
    res = eval(s0)
    value_1 = int(combo2.get())
    calc.insert(0, system_convert.convert_10_to_n(res, value_1))


def clear():
    calc.delete(0, tk.END)


def add_operation(operation):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def operation_button(operation):
    return tk.Button(text=operation, bd=5, fg='red', font=(20), command=lambda: add_operation(operation))


def alike_button(operation):
    return tk.Button(text=operation, bd=5, fg='red', command=calculate)


def clear_button(operation):
    return tk.Button(text=operation, bd=5, fg='red', command=clear)


win = tk.Tk()
win.geometry(f"720x300+100+200")
win['bg'] = '#33ffe6'
win.title('Калькулятор')


labelTop = tk.Label(win, text='В какой системе счисления хотите видеть первое число:')
labelTop.grid(row=0, column=0, sticky='wens', padx=5, pady=7)


nums = [i for i in range(2, 17)]
combo = ttk.Combobox(win, values=nums)
combo.grid(row=1, column=0, sticky='wens', padx=5, pady=7)


labelTop1 = tk.Label(win, text='В какой системе счисления хотите видеть второе число:')
labelTop1.grid(row=0, column=1, sticky='wens', padx=5, pady=7)


combo1 = ttk.Combobox(win, values=nums)
combo1.grid(row=1, column=1, sticky='wens', padx=5, pady=7)


calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=2, column=0, columnspan=3, sticky='we', padx=5)


labelTop2 = tk.Label(win, text='В какой системе счисления хотите получить ответ:')
labelTop2.grid(row=3, column=1, sticky='wens', padx=5, pady=7)


combo2 = ttk.Combobox(win, values=nums)
combo2.grid(row=4, column=1, sticky='wens', padx=5, pady=7)


operation_button('+').grid(row=5, column=0, sticky='wens', padx=5, pady=7)
operation_button('-').grid(row=5, column=1, sticky='wens', padx=5, pady=7)
operation_button('*').grid(row=6, column=1, sticky='wens', padx=5, pady=7)
operation_button('/').grid(row=6, column=0, sticky='wens', padx=5, pady=7)


alike_button('=').grid(row=6, column=2, sticky='wens', padx=5, pady=7)
clear_button('C').grid(row=5, column=2, sticky='wens', padx=5, pady=7)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)

win.grid_rowconfigure(0, minsize=60)


win.mainloop()


def main():
    pass

if __name__=='__main__':
    main()








