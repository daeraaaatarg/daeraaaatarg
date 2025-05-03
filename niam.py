print("hello world")

a = float(input("Перше число: "))
b = float(input("Друге число: "))
op = input("Операція (+, -, *, /): ")

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b != 0:
        print("Результат:", a / b)
    else:
        print("Помилка: ділення на нуль!")
else:
    print("Невідома операція")