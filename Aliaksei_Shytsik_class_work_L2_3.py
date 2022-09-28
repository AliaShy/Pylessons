# # Классная работа № 3 (21.09.2022).

# # Пример использования операторов:
# n = int(input("Enter a number: "))

# print(n > 100)  # False.
# print(n < 100)  # True.
# print(n == 55)  # False.
# print(n != 55)  # True.
# print(n >= 100)  # False.
# print(n <= 100)  # True.


# # Пример использования операторов:
# x = 10
# y = 20
# z = 20
# print(x == y)  # False.
# print(z == y)  # True.
# print(x != y)  # True.
# print(x > 20)  # False.
# print(x < y)  # True.
# print(x >= 10)  # True.
# print(y <= 20)  # True.


# # Так можно определить тип переменной:
# print(x, type(x))


# # Простейший пример использования оператора if:
# a = 33
# b = 200
# if b > a:
#     print("b is bigger than a")  # Результат выполнения - вывод сообщения.


# # Пример использования оператора if-else:
# amount = int(input("Enter amount: "))

# if amount < 1000:
#     discount = amount * 0.05  # Выполняется, если условие истинно.
#     print("Discount", discount)
# else:
#     discount = amount * 0.10  # Выполняется, если условие ложно.
#     print("Discount", discount)

# print("Net payable:", amount-discount)


# # Пример использования elif:
# amount = int(input("Enter amount: "))

# if amount < 1000:
#     discount = amount * 0.05  # Выполняется, если условие истинно.
#     print("Discount", discount)
# elif amount < 5000:
#     discount = amount * 0.10  # Выполняется, если введенная переменная меньше 5000, но больше 1000.
#     print("Discount", discount)
# else:
#     discount = amount * 0.15  # Выполняется, если ни одно из вышеуказанных условий не выполнились.
#     print("Discount", discount)

# print("Net payable:", amount-discount)


# # Пример сранения двух чисел:
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Выбор наибольшего числа.
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# # Вывод результата выбора.
# print("The larger number is:", larger_number)


# # Простое условие:
# largest_number = -999999999
# number = int(input("Введите число: "))
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number


# ## Простой бесконечный цикл while:
# #while True:
# #    print("I'm stuck inside the loop.")  # Выполняется пока условие True, и, посколько оно не переопределяется, оно True всегда.


# # Конечный цикл while:
# count = 0  # Присваиваем переменной нулевое значение.
# while (count < 9):  # Устанавливаем условие выполнения цикла (пока значение переменной меньше 9).
#     print('The count is: ', count)  # Выводим значение переменной (повторяется, пока не достигнет 8).
#     count += 1  # Увеличиваем значение переменной на 1.

# print("Good bye!")


# # Пример цикла с условием: 
# largest_number = -999999999  # Присваивает переменной минимального отрицательное число.
# number = int(input("Enter a number or type -1 to stop: "))  # Передает переменной введенное пользователем число.
# while number != -1:  # Условие для выполнения цикла - пока пользователь не ввел -1.
#     if number > largest_number:  # Проверяем условие, больше ли введенное пользователем число минимального, присвоенного изначально переменной largest_number. 
#         largest_number = number  # Если условие выполняется, присваиваем переменной largest_number введенное пользователем число.
#     number = int(input("Enter a number or type -1 to stop: "))  # Предлагаем пользователю еще раз ввести число.
# print("The largest number is: ", largest_number)  # Если пользователь ввел -1 - выходим из цикла. и выводим максимальное из введенных пользователем чисел.


# # Скрипт подсчета количества введенных четных и нечетных чисел:
# # Устанавливаем счетчики четных и нечетных чисел в 0.
# odd_numbers = 0
# even_numbers = 0

# # Предложение пользователю ввести число, значение которого присваивается переменной number.
# number = int(input("Enter a number or type 0 to stop: "))

# while number != 0:  # Устанавливаем условие выполнения цикла (пока не введен 0).
#     if number % 2 == 1:  # Проверка на четность, если остаток от деления равен 1 - нечетное.
#         odd_numbers += 1  # Увеличение на 1 счетчика нечетных чисел.
#     else:
#         even_numbers += 1  # увеличение на 1 счетчика четных чисел (выполняется, если условие выше ложно).
#     number = int(input("Enter a number or type 0 to stop: "))  # Повторно предлагаем пользователю ввести число, значение которого присваивается переменной number.

# # Вывод результатов подсчета.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)


# # Цикл while c выходом из петли:
# counter = 5  # Присваиваем переменной-счетчику значение5.

# while counter != 0:  # Устанавливаем условие выполнение цикла, пока счетчик не станет равен 0.
#     print("Inside the loop.", counter)  # Вывод сообщения в случае, если условие True.
#     counter -= 1  # Уменьшение счетчика на 1.
# print("Outside the loop.", counter)  # Вывод сообщения в случае, если условие False.


# # Пример использования цикла for:
# for i in range(10):
#     print("The value of i is currently:", i)  # Выведет значения от 0 до 9.


# # Еще один пример использования цикла for:
# for i in range(2, 8):
#     print("The value of i is currently:", i)  # Выведет значения от 2 до 7.


# # Пример использования цикла for:
# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2


# # Пример использования for и list:
# for var in list(range(5)):
#     print(var)  # Вывод листа (переменные выводятся в столбик).


# # Пример использования for в заданном диапазоне значений:
# for x in range(2, 6):
#     print(x, end=" ")


# # Пример использования for в заданном диапазоне значений и с заданным шагом:
# for x in range(2, 30, 3):
#     print(x, end=" ")

# # Пример использования оператора break (прерывание цикла):
# print("The break instruction: ")
# for i in range (1, 6):  # Задаем диапазон значений для счетчика.
#     if i == 3:  # Задаем условие, при соответствии переменной счетчика которому, цикл прервется.
#         break
#     print("Inside the loop.", i)  # Выполняется в случае, если цикл выполняется.
# print("Outside the loop.")  # Выполняется в случае, если произошел выход из цикла.


# # Пример использования оператора continue (продолжение цикла):
# print("\nThe continue instruction:")
# for i in range(1, 6):  # Задаем диапазон значений для счетчика.
#     if i == 3:  # Задаем условие, при соответствии переменной счетчика которому, цикл продолжит выполняться минуя его.
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")


# # Пример использования break:
# largest_number = -999999999  # Присваиваем переменной наименьшее число.
# counter = 0  # Устанавливаем счетчик в 0.

# while True:  # Устанавливаем условие выполнения цикла.
#     number = int(input("Enter a number or type -1 to end program: "))  # Предложение пользователю ввести число.
#     if number == -1:  # Устанавливаем условие прерывания цикла.
#         break 
#     counter += 1  # Увеличиваем значение счетчика на 1.
#     if number > largest_number:  # Сравниваем введенное пользователем число с наименьшим, присвоенным переменной largest_number.
#         largest_number = number  # Присваиваем переменной largest_number значение введенного пользователем числа в случае, если оно оказалось больше.

# if counter != 0:
#     print("The largest number is:", largest_number)
# else:
#     print("You have not entered any number.")  # Если пользователь ввел 0.


#     # Пример использования оператора continue.
# largest_number = -999999999
# counter = 0

# number = int(input("Enter a number or type -1 to end program: "))  # Предложение пользователю ввести число.
# while number != -1:  # Устанавливаем условие выполнения цикла - пока пользователь не введет -1.
#     if number == -1:
#         continue
#     counter += 1

#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))  # Повторное предложение пользователю ввести число.

# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")


# # Цикл while с ветвлением else:
# numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]

# for num in numbers:  # Устанавливаем условие выполнение цикла - все значения из списка numbers.
#     if num % 2 == 0:  # Проверяем на четность.
#         print("The list contains an even number.")  # Выводится, если найдено четное число.
#         break  # Выполнение цикла прерывается.
# else:
#     print("The list does not contain even number.")  # Выводится, если четное число не найдено.


# # Еще один пример использования цикла while с ветвлением else:
# count = 0  # Устанавливаем счетчик в 0.
# while count < 5:  # Устанавливаем условие выполнения цикла - пока счетчик не достигнет 5.
#     print(count, "is less than 5")  # Выводится, пока цикл выполняется.
#     count += 1  # Значение счетчика увеличивается на 1.
# else:
#     print(count, "is not less than 5")  # Выполняется по выходу из цикла.


# # Пример, аналогичный предыдущему (оставлю без комментариев):
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else:", i)


# # Пример использования логического оператора and:
# i = 0
# x = 0
# while(i < 10 and x < 5):  # Задаем условие выполнения цикла - i < 10 И x < 5.
#     x = i  # Присваиваем переменной x значение переменной i.
#     print(i, end=" ")  # Выводим значение переменной i.
#     i += 1  # Увеличиваем счетчик на 1.


# # Еще один пример использования логического оператора and:
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print("Both conditions are True.")


# # Пример использования логического оператора or:
# a = 200
# b = 33
# c = 500
# if a > b or a > c:  # Задаем условие выполнения.
#     print("At least one of the conditions is True.")


# # Еще один пример использования логического оператора or:
# i = 0
# x = 0
# while(i < 10 or x < 5):  # Задаем условие выполнения цикла - i < 10 ИЛИ x < 5.
#     x = i  # Присваиваем переменной x значение переменной i.
#     print(i, end=" ")  # Выводим значение переменной i.
#     i += 1  # Увеличиваем счетчик на 1.
