#переменные
number1 = float(input("Введите первое число "))
number2 = float(input("Введите второе число "))      
move = input("Выберите действие (+,-,*,/) ")


#if/elif
if move == "+":
    result = number1 + number2
elif move == "-":
    result = number1 - number2
elif move == "*":
    result = number1 * number2
elif move == "/":
    if number1 == 0 or number2 == 0:
        result = ("Ты помойму перепутал")
    else:
        result = number1 / number2
else:
    print('Переделывай')



#результат
print("Ваш ответ: ", result)
input("Нажмите Enter для выхода")