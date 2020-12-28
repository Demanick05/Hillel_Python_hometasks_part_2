import tkinter as tk


def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))


def make_digit(digit):
    return tk.Button(text=digit, bd=5, command=lambda: add_digit(digit))


def make_operation(operation):
    return tk.Button(text=operation, bd=5, command=lambda: add_operation(operation))


def calculate_button(operation):
    return tk.Button(text=operation, bd=5, command=calculate())


win = tk.Tk()
win.geometry("240x260+100+200")
win['bg'] = '#0c256a'
win.title('Calculator')

calc = tk.Entry(win, justify=tk.RIGHT)
calc.grid(row=0, column=0, columnspan=4, stick="we")

make_digit('1').grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit('2').grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit('3').grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit('4').grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit('5').grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit('6').grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit('7').grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit('8').grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit('9').grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit('0').grid(row=4, column=0, columnspan=2, stick="wens", padx=5, pady=5)

make_operation('+').grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation('-').grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation('/').grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation('*').grid(row=4, column=3, stick="wens", padx=5, pady=5)

calculate_button('=').grid(row=4, column=2, stick="wens", padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
