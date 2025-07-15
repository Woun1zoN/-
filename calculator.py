while True:
    a = input("Введите число: ")
    try:
        число = float(a)
        print(f"Вы ввели: {число}")
        break
    except ValueError:
        print("Вы ввели не числовое значение!")

while True:
    op = input("""Выберите математическую операцию: 
+ : Сложение
- : Вычитание
* : Умножение
/ : Деление
Ваш выбор: """)
    if op in ['+', '-', '*', '/', ':']:
        break
    else:
        print("Вы ввели не математическую операцию!")

while True:
    b = input("Введите второе число: ")
    try:
        число2 = float(b)
        print(f"Вы ввели: {число2}")
        break
    except ValueError:
        print("Вы ввели не числовое значение!")

if op == "+":
    print(f"Результат: {число + число2}")
elif op == "-":
    print(f"Результат: {число - число2}")
elif op == "*":
    print(f"Результат: {число * число2}")
elif op == "/":
    print(f"Результат: {число / число2}") if b != 0 else print("На ноль делить нельзя!")
elif op == ":":
    print(f"Результат: {число / число2}") if b != 0 else print("На ноль делить нельзя!")
else:
    print(f"Неверная операция")
