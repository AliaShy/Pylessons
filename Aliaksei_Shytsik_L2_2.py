# # Домашняя работа:

# # Home work 2.1:
# # Получаем значения переменных:
# a = float(input("Enter the 'A' number: "))
# b = float(input("Enter the 'B' number: "))
# c = float(input("Enter the 'C' number: "))
# d = float(input("Enter the 'D' number: "))

# # Находим наибольшее число в первой паре введенных.
# if a > b:
#     pair1 = a
# else:
#     pair1 = b
# # Находим наибольшее число во второй паре введенных.
# if c > d:
#     pair2 = c
# else:
#     pair2 = d
# # Сравниваем наибольшие найденные в парах числа между собой, находим наибольшее.
# if pair1 > pair2:
#     print("The largest number is: ", pair1)
# else:
#     print("The largest number is: ", pair2)


# # Home work 2.2:
# # Получаем значения переменных.
# a = float(input("Enter the 'a' number: "))
# b = float(input("Enter the 'b' number: "))
# c = float(input("Enter the 'c' number: "))
# d = float(input("Enter the 'd' number: "))
# e = float(input("Enter the 'e' number: "))
# f = float(input("Enter the 'f' number: "))

# # Находим максимальное и минимальное число из введенных, выводим результат.
# print("Максимальное число из введенных: ", max(a, b, c, d, e, f))  # Максимальное число из введенных.
# print("Минимальное число из введенных: ", min(a, b, c, d, e, f))  # Минимальное число из введенных.


# # Home work 2.3:
# input_string = input("Print the plant: ")  # Принимаем вводимое значение в переменную.

# if input_string == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")  # Данное сообщение будет выведено, если введено Spathiphyllum.
# elif input_string == "spathiphyllum":
#     print("No, I want a big Spathiphyllum")  # Данное сообщение будет выведено, если введено spathiphyllum.
# else:
#     print("Spathiphyllum! Not", input_string)  # Данное сообщение будет выведено, в любом ином случае.


# # Home work 2.4:
# input_year = int(input("Enter the year: "))  # Принимаем вводимое значение года в переменную.
# if input_year >= 1582:  # Условие проверки, входит ли введенный год в Григорианский календарь.
#     if input_year % 4 != 0:  # Первое условие проверки, является ли год НЕ високосным.
#         print("Common year.")
#     elif input_year % 100 != 0: # Второе условие проверки, является ли год високосным. 
#         print("Leap year.")
#     elif input_year % 400 != 0:  # Третее условие проверки, является ли год НЕ високосным.
#         print("Common year.")
#     else:
#         print("Leap year")  # Выводится, если ни одно из вышеперечисленных условий не выполнено.
# else:
#     print("Not within the Gregorian calendar period")  # Выводится, если введенный год не входит в Григорианский календарь.


# # Home work 2.5:
# import time  # Импортируем библиотеку времени.
# count = 1  # Устанавливаем счетчик в значение 1.
# while count <= 5:  # Устанавливаем условие выполнения цикла (пока счетчик не достигнет 5 включительно).
#     print(count, "Mississippi")  # Выводим значение.
#     time.sleep(1)  # Устанавливаем задержку по времени в 1 секунду.
#     count += 1  # Увеличиваем значение счетчика на 1.

# print("Ready or not, here I come!")  # Фраза выводится по завершении выполнения цикла.


# # Home work 2.6:
# user_word = input("Enter the word: ")  # Запрос ввода слова.
# letter = user_word.upper()  # Преобразование введенного слова в верхний регистр.

# for i in letter:  # Задаем условие выполнения цикла - для всех символов, содержащихся в переменной letter.
#     if i in "EYUIOA":  # Устанавливаем условие пропуска буквы (все гласные).
#         continue
#     print(i)  # Выводим на печать все оставшиеся (согласные).
