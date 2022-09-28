# # Домашняя работа № 3:

# # Home work 3.1:
# hat_list = [1, 2, 3, 4, 5]

# print(len(hat_list))  # Выводим длину листа.
# userNumber = int(input("Enter the number, that would replace the middle number of the list: "))  # Предложение пользователю ввести число.

# hat_list[2] = userNumber  # Заменяем среднее значение в листе на введенное пользователем.
# print("New hat_list is:", hat_list)  # Выводим новый лист.

# del hat_list[-1]  # Удаляем последнее значение листа.
# print("New hat_list with deleted value is:", hat_list)  # Выводим новый лист.

# print(len(hat_list))  # Выводим длину листа.


# # Home work 3.2:
# # Step 1.
# beatles = []  # Создаем пустой список.
# print("Step 1: The members of the Beatles band are:", beatles)

# # Step 2.
# beatles.append('John Lennon')  # Добавляем в состав John Lennon.
# beatles.append('Paul McCartney')  # Добавляем в состав Paul McCartney.
# beatles.append('George Harrison')  # Добавляем в состав George Harrison.
# print("Step 2: The members of the Beatles band are:", beatles)

# # Step 3.
# for i in range(2):  # Задаем условие выполнения цикла - 2 раза.
#     newMember = input("Would you like to add anyone to the Beatles band? ")  # Предлагаем пользователю ввести нового члена группы.
#     beatles.append(newMember)  # Добавляем введенного пользователем члена группы в конец списка.
# print("Step 3: The members of the Beatles band are:", beatles)

# # Step 4.
# beatles.remove('Stu Sutcliffe')  # Удаляем Stu.
# beatles.remove('Pete Best')  # Удаляем Pete.
# print("Step 4: The members of the Beatles band are:", beatles)

# # Step 5.
# beatles.insert(0, 'Ringo Starr')  # Добавляем в состав Ringo Starr.
# print("Step 5: The members of the Beatles band are:", beatles)


# # Home work 3.3 (с использованием пузырьковой сортировки):
# my_list = []  # Создаем пустой список.

# swapped = True  # Устанавливаем переменную, которая будет использоваться для прерывания while в True.
# n = int(input('How many numbers should the list consist? '))  # Предлагаем пользователю ввести количество значений в списке.

# for i in range(n):  # Устанавливаем условие для цикла запросов на ввод значений в список.
#     listNumber = int(input('Type the number '))  # Запрос на ввод значения для для списка.
#     i += 1
#     my_list.append(listNumber)  # Добавление введенного пользователем числа в конец списка.

# print(my_list)  # Вывод сформированного списка.

# sortType = input('What type of sort would you like, INCREASED (type: inc) or REVERSED (type: rev)? ')  # Предложение пользователю ввести тип сортировки.

# # Цикл в зависимости от выбранного пользователем типа сортировки.
# # Если выбрана сортировка по возрастанию.
# if sortType == 'inc':
#     while swapped:  # Устанавливаем условие выполнения цикла while.
#         swapped = False  # Присваиваем переменной swapped значение False.
#         for i in range(len(my_list) - 1):  # Устанавливаем условие выполнения цикла for - для всех i от 0 до 4, т.е. для всех значений листа.
#             if my_list[i] > my_list[i + 1]:  # Если iтый элемент >  элемента i+1.
#                 swapped = True  # Переменной присваивается значение true для продолжения выполнения цикла.
#                 my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Элементу i присваивается значение элемента i+1, а элементу i+1 - значение элемента i.
#     print(my_list)  # По выходу из цикла выводим отсортированный список.

# # Если выбрана сортировка по убыванию.
# elif sortType == 'rev':
#     while swapped:  # Устанавливаем условие выполнения цикла while.
#         swapped = False  # Присваиваем переменной swapped значение False.
#         for i in range(len(my_list) - 1):  # Устанавливаем условие выполнения цикла for - для всех i от 0 до 4, т.е. для всех значений листа.
#             if my_list[i] < my_list[i + 1]:  # Если iтый элемент <  элемента i+1.
#                 swapped = True  # Переменной присваивается значение true для продолжения выполнения цикла.
#                 my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Элементу i присваивается значение элемента i+1, а элементу i+1 - значение элемента i.
#     print(my_list)  # По выходу из цикла выводим отсортированный список.

# # Если пользователем введено неверное значение при выборе типа сориторвки.
# else:
#     print('The choice was incorrect')


# # Home work 3.3 (с использованием методов):
# my_list = []  # Создаем пустой список.

# swapped = True  # Устанавливаем переменную, которая будет использоваться для прерывания while в True.
# n = int(input('How many numbers should the list consist? '))  # Предлагаем пользователю ввести количество значений в списке.

# for i in range(n):  # Устанавливаем условие для цикла запросов на ввод значений в список.
#     listNumber = int(input('Type the number '))  # Запрос на ввод значения для для списка.
#     i += 1
#     my_list.append(listNumber)  # Добавление введенного пользователем числа в конец списка.

# print(my_list)  # Вывод сформированного списка.

# sortType = input('What type of sort would you like, INCREASED (type: inc) or REVERSED (type: rev)? ')  # Предложение пользователю ввести тип сортировки.

# # Цикл в зависимости от выбранного пользователем типа сортировки.
# # Если выбрана сортировка по возрастанию.
# if sortType == 'inc':
#     my_list.sort()
#     print(my_list)  # По выходу из цикла выводим отсортированный список.

# # Если выбрана сортировка по убыванию.
# elif sortType == 'rev':
#     my_list.sort()
#     my_list.reverse()
#     print(my_list)  # По выходу из цикла выводим отсортированный список.

# # Если пользователем введено неверное значение при выборе типа сориторвки.
# else:
#     print('The choice was incorrect')


# # Home work 3.4:
# source_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9, 9, 0]  # Создаем исходный список.
# result_list = []  # Создаем итоговый пустой список, куда будем вносить отсортированные значения.
# for i in source_list:  # Условие выполнения цикла while - для всех значений исходного списка.
#     if i not in result_list:  # Если значение из исходного списка отсутствует в итоговом.
#         result_list.append(i)  # То добавляем это значение в конец итогового списка.
#         i += 1  # Переход к следующему значению исходного списка.
# print(result_list)  # Вывод результата по выходу из цикла.
