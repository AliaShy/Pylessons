# # Домашняя работа № 1:

# # Home work 1.0:
# print("Hello, Python!")  # Отображение на устройстве вывода надписи "Hello, Python".

# print("Aliaksei")  # Отображение на устройстве вывода собственного имени.

# # print(Aliaksei) # Без "" Aliaksei воспринимается как переменная. При исполнении скрипта выводится сообщение о том, что переменная не определена.

# # print "Aliaksei" # Python обнаружил ошибку в виде отсутствия "()" в функции print и предлагает использовать print().

# print('Aliaksei')  # Отображение на устройстве вывода собственного имени (в одинарных кавычках работает как и в двойных).

# print("Hello, Python!"), print("Aliaksei"), print("Shytsik")  # Использование нескольких функций print на одной строке. Результат выполнения каждой отображается с новой строки.

# # Использование нескольких функций print в разных строках. Результат выполнения каждой отображается с новой строки:
# print("Hello, Python!")
# print("Aliaksei")
# print("Shytsik") 

# # Home work 1.1:
# print("Programming", "Essentials", sep="***", end="***")  # Вывод аргументов через "***", завершается вывод символами "***".
# print("in", "Python", sep="...")  # Вывод аргументов через "..." в той же строке, в которой были выведены аргументы предыдущей функции.

# # Home work 1.2:
# # Исходный вариант:
# print("    *")
# print("   * *")
# print("  *   *")
# print(" *     *")
# print("***   ***")
# print("  *   *")
# print("  *   *")
# print("  *****")

# # Модифицированный вариант с sep и end:
# print("    *", end="\n   ")
# print("*", "*", end="\n  ")
# print("*", "*", sep="   ", end="\n ")
# print("*", "*", sep="     ", end="\n")
# print("***", "***", sep="   ", end="\n  ")
# print("*", "*", sep="   ", end="\n  ")
# print("*", "*", sep="   ", end="\n  ")
# print("*****")

# # Вариант в 2 строки:
# print("    *\n", "  * *\n", " *   *\n", "*     *")
# print("***   ***\n", " *   *\n", " *   *\n", " *****")

# # Home work 1.3:
# print('"I\'m"', '""learning""', '"""Python"""', sep="\n") # Выводит каждый аргумент с новой строки. 1 строка в двойных кавычках, 2 - в двух двойных, 3 - в трех двойных кавычках.

# # Home work 1.4:
# Adam = 1  # Присваиваем значение переменной Adam.
# John = 3  # Присваиваем значение переменной John.
# Mary = 5  # Присваиваем значение переменной Mary.
# print("Adam", "Jonh", "Mary", sep=", ")  # Выводим имена переменных в одну строку, разделяя запятыми.
# total_apples = (Adam + John + Mary)  # Объявляем переменную total_apples и присваиваем ей результат суммы всех яблок.
# apples_per_person = (total_apples / 3)  # Объявляем переменную apples_per_person и присваиваем ей результат среднего количества яблок на человека.
# max_apples = (max (Adam, John, Mary))  # Объявляем переменную max_apples и присваиваем ей результат вычисления максимального количества яблок у одного человека.
# min_apples = (min (Adam, John, Mary))  # Объявляем переменную min_apples и присваиваем ей результат вычисления минимального количества яблок у одного человека.
# print("Apples at all =", total_apples, "Average amount of apples =", apples_per_person, "Max apples per person =", max_apples, "Min apples per person =", min_apples)  # Выводим значения вычислений.
# print('Apples at all = {0}, Average amount of apples = {1}, Max apples per person = {2}, Min apples per person = {3}'.format(total_apples, apples_per_person, max_apples, min_apples))  # Выводим значения вычислений (2 способ).

# # Home work 1.5:
# kilometers = 12.25  # Объявляем переменную kilometers и присваиваем ей значение.
# miles = 7.38  # Объявляем переменную miles и присваиваем ей значение.

# mls_in_km = kilometers / 1.61  # Присваиваем реззультат вычисления количества миль в километрах переменной mls_in_km.
# km_in_mls = miles * 1.61  # Присваиваем результат вычисления количетсва километров в милях переменной km_in_mls.

# res_mik = round(mls_in_km, 2)  # Округляем результат вычисления миль в километрах до сотых.
# res_kim = round(km_in_mls, 2)  # Округляем результат высисления километров в милях до сотых.
# print(miles, "miles is", res_kim, "kilometers")  # Выводим результат вычисления количества километров в милях.
# print(kilometers, "kilometers is", res_mik, "miles")  # Выводим результат вычисления количества миль в километрах.
