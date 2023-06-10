from tkinter import *

root = Tk()    # Создание окна программы
root.title('Калькулятор квартплаты')    # Название программы
root.resizable(width=False, height=False)    # Запрет на изменение размеров окна. Просто эстетическая сторона вопроса)

water_label = Label(text='Водоснабжение (м.куб.)')    # Название для поля ввода
water_label.grid(row=1, column=0, sticky='w', padx=(30, 0))    # Расположение названия поля
water = StringVar()    # Задание формата данных для поля ввода
e1 = Entry(textvariable=water)    # Создание поля ввода с обозначенным ранее форматом данных
e1.grid(row=1, column=3, sticky='ew', padx=(0, 30))    # Расположение поля ввода
heat_label = Label(text='Отопление (Гкал.)')
heat_label.grid(row=2, column=0, sticky='w', padx=(30, 0))
heat = StringVar()
e2 = Entry(textvariable=heat)
e2.grid(row=2, column=3, sticky='ew', padx=(0, 30))
electricity_label = Label(text='Электричество (кВт/ч)')
electricity_label.grid(row=3, column=0, sticky='w', padx=(30, 0))
electricity = StringVar()
e3 = Entry(textvariable=electricity)
e3.grid(row=3, column=3, sticky='ew', padx=(0, 30))
t = Text(root, height=10)
t.grid(row=9, column=0, columnspan=4, sticky='nesw', padx=30)
gas_label = Label(text='Газоснабжение (м.куб.)')
gas_label.grid(row=4, column=0, sticky='w', padx=30)
gas = StringVar()
e4 = Entry(textvariable=gas)
e4.grid(row=4, column=3, sticky='ew', padx=(0, 30))
water_out_label = Label(text='Водоотведение (м.куб.)')
water_out_label.grid(row=5, column=0, sticky='w', padx=(30, 0))
water_out = StringVar()
e5 = Entry(textvariable=water_out)
e5.grid(row=5, column=3, sticky='ew', padx=(0, 30))
square_label = Label(text='Кап.ремонт + Лифт => Площадь (м.кв.)')
square_label.grid(row=6, column=0, sticky='w', padx=(30, 0))
square = StringVar()
e6 = Entry(textvariable=square)
e6.grid(row=6, column=3, sticky='ew', padx=(0, 30))
result_label = Label(text='Итог (бел.руб.):')
result_label.grid(row=8, column=0, sticky='w', padx=30)

tariff_label = Label(text='Тариф (бел.руб):')
tariff_label.grid(row=0, column=1, sticky='ew', padx=(0, 30), pady=(10, 0))
water_tariff = StringVar(value='1.3542')    # Задание значения по умолчанию в поле для ввода
e7 = Entry(textvariable=water_tariff, state='disabled',
           disabledbackground='white', justify=CENTER, disabledforeground='black')
e7.grid(row=1, column=1, sticky='ew', padx=(0, 30))
heat_tariff = StringVar(value='21.9245')
e8 = Entry(textvariable=heat_tariff, state='disabled',
           disabledbackground='white', justify=CENTER, disabledforeground='black')
e8.grid(row=2, column=1, sticky='ew', padx=(0, 30))
electricity_tariff = StringVar(value='0.209')
e9 = Entry(textvariable=electricity_tariff, state='disabled',
           disabledbackground='white', justify=CENTER, disabledforeground='black')
e9.grid(row=3, column=1, sticky='ew', padx=(0, 30))
gas_tariff = StringVar(value='0.5477')
e10 = Entry(textvariable=gas_tariff, state='disabled',
           disabledbackground='white', justify=CENTER, disabledforeground='black')
e10.grid(row=4, column=1, sticky='ew', padx=(0, 30))
water_out_tariff = StringVar(value='1.1312')
e11 = Entry(textvariable=water_out_tariff, state='disabled',
           disabledbackground='white', justify=CENTER, disabledforeground='black')
e11.grid(row=5, column=1, sticky='ew', padx=(0, 30))
square_tariff = StringVar(value='0,2138 + 0.0699')
e12 = Entry(textvariable=square_tariff, state='disabled',
           disabledbackground='white', justify=CENTER, disabledforeground='black')
e12.grid(row=6, column=1, sticky='ew', padx=(0, 30))

e1.config(state='disabled')    # Присваивание полю ввода неактивного значения по умолчанию
e2.config(state='disabled')
e3.config(state='disabled')
e4.config(state='disabled')
e5.config(state='disabled')
e6.config(state='disabled')


def ch_box():    # Функция для обновления состояния поля ввода в зависимости от значения чекбокса
    if var1.get() == 1:
        e1.update()
        e1.config(state='normal')
    else:
        e1.config(state='disabled')
    if var2.get() == 1:
        e2.update()
        e2.config(state='normal')
    else:
        e2.config(state='disabled')
    if var3.get() == 1:
        e3.update()
        e3.config(state='normal')
    else:
        e3.config(state='disabled')
    if var4.get() == 1:
        e4.update()
        e4.config(state='normal')
    else:
        e4.config(state='disabled')
    if var5.get() == 1:
        e5.update()
        e5.config(state='normal')
    else:
        e5.config(state='disabled')
    if var6.get() == 1:
        e6.update()
        e6.config(state='normal')
    else:
        e6.config(state='disabled')


var1 = IntVar()    # Тип данных для чекбокса (1 или 0)
c1 = Checkbutton(root, variable=var1, onvalue=1, offvalue=0, command=ch_box)    # Задание чекбокса и его св-в
c1.grid(row=1, column=2)    # Расположения чекбокса в 1-ой(2) строке 2-ой(3) колонки
var2 = IntVar()
c2 = Checkbutton(root, variable=var2, onvalue=1, offvalue=0, command=ch_box)
c2.grid(row=2, column=2)
var3 = IntVar()
c3 = Checkbutton(root, variable=var3, onvalue=1, offvalue=0, command=ch_box)
c3.grid(row=3, column=2)
var4 = IntVar()
c4 = Checkbutton(root, variable=var4, onvalue=1, offvalue=0, command=ch_box)
c4.grid(row=4, column=2)
var5 = IntVar()
c5 = Checkbutton(root, variable=var5, onvalue=1, offvalue=0, command=ch_box)
c5.grid(row=5, column=2)
var6 = IntVar()
c6 = Checkbutton(root, variable=var6, onvalue=1, offvalue=0, command=ch_box)
c6.grid(row=6, column=2)


def calculate():    # Функция для рассчёта и вывода конечного результата

    if var1.get() == 1:    # Условие получения
        if len(water.get()) == 0:    # Защита. Если поле пустое, то ему присваивается значение 0.0
            x = 0.0
        else:
            x = float(water.get())    # Получение введённых в поле данных
    else:
        e1.config(state='disabled')    # Вариант, когда пользователь хочет проигнорировать данное поле
        x = 0.0    # Зануление значения поля по умолчанию
    if var2.get() == 1:
        if len(heat.get()) == 0:
            y = 0.0
        else:
            y = float(heat.get())
    else:
        e2.config(state='disabled')
        y = 0.0
    if var3.get() == 1:
        if len(electricity.get()) == 0:
            z = 0.0
        else:
            z = float(electricity.get())
    else:
        e3.config(state='disabled')
        z = 0.0
    if var4.get() == 1:
        if len(gas.get()) == 0:
            a = 0.0
        else:
            a = float(gas.get())
    else:
        e4.config(state='disabled')
        a = 0.0
    if var5.get() == 1:
        if len(water_out.get()) == 0:
            b = 0.0
        else:
            b = float(water_out.get())
    else:
        e5.config(state='disabled')
        b = 0.0
    if var6.get() == 1:
        if len(square.get()) == 0:
            c = 0.0
        else:
            c = float(square.get())
    else:
        e6.config(state='disabled')
        c = 0.0
    print(x)
    water_bill = x * 1.3542    # Математические операции над введёнными данными
    heating_bill = y * 21.9245
    electricity_bill = z * 0.209
    gas_bill = a * 0.5477
    water_out_bill = b * 1.1312
    square_bill = c * (0.2138 + 0.0699)

    sum_bill = water_bill + heating_bill + electricity_bill + gas_bill + water_out_bill + square_bill
    sum_bill = f'Счёт за водоснабжение по тарифу 1.3542 руб. за м.куб.: {water_bill} бел.руб.' + \
               f'\nСчёт за отопление по тарифу 21.9245 руб. за Гкал.: {heating_bill} бел.руб.' + \
               f'\nСчёт за электричество по тарифу 0.209 руб. за кВт/ч: {electricity_bill} бел.руб.' + \
               f'\nСчёт за газ по тарифу 0.5477 руб. за м.куб.: {gas_bill} бел.руб.' + \
               f'\nСчёт за отвод воды по тарифу 1.1312 руб. за м.куб.: {water_out_bill} бел.руб.' + \
               f'\nСчёт за кап.ремонт и обсл.лифта по тарифу (0.2138 + 0.0699) руб. за м.кв.: {square_bill} бел.руб.\n'\
               + f'\nВсего подлежит к оплате: {sum_bill} бел.руб.'
    # res = sum_bill
    print(sum_bill)
    t.config(state='normal')    # Обозначение возможности редактировать текстовое поле ИТОГ
    t.delete(1.0, END)
    t.insert(1.0, sum_bill)    # Заполнение поля результатом математических операций
    t.config(state='disabled')    # Возвращение полю нередактируемого формата
    with open('Итог.txt', 'w') as result_file:
        result_file.write(sum_bill)


button = Button(root, text='Рассчитать стоимость', font=('Helvetica', '12', 'normal'), command=calculate, width=30)
# Создание кнопки залинкованной к функции calculate
button.grid(row=7, columnspan=4, pady=10)    # Размещаем кнопку в 5 строке программы и заполняем 4 столбца

root.grid_columnconfigure(0, minsize=200, pad=50)
root.grid_columnconfigure(1)
root.grid_columnconfigure(2)
root.grid_columnconfigure(3, minsize=200, pad=50)
root.grid_rowconfigure(0, minsize=24)
root.grid_rowconfigure(1, minsize=24)
root.grid_rowconfigure(2, minsize=24)
root.grid_rowconfigure(3, minsize=24)
root.grid_rowconfigure(4, minsize=24)
root.grid_rowconfigure(5, minsize=24)
root.grid_rowconfigure(6, minsize=24)
root.grid_rowconfigure(7, minsize=24)
root.grid_rowconfigure(8, minsize=24)

root.mainloop()    # Зацикливание программы, чтобы сразу не закрывалась
