from logger import input_data, print_data, put_data, delete_data
# В этой функции происходит взаимодействие пользователя с консолью
# мы выводим ему приветствие и список того что можно сделать в нашей программе
# и на основе его ввода мы запускаем необходимую часть программы
def interface():
    # -1 просто для того чтобы запустился цикл
    command = -1
    while command != 5:
        print('Здравствуйте! Что для Вас нужно сделать? \n'
              '1. Записать данные \n'
              '2. Удалить данные \n'
              '3. Изменить данные\n'
              '4. Вывести данные\n'
              '5. Выход')
        command = int(input("Введите номер операции: "))

        while command < 1 or command > 5:
            print('Ошибка! Попробуйте еще раз')
            command = int(input("Введите номер операции: "))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            put_data()
        elif command == 4:
            delete_data()
        elif command == 5:
            print("Спасибо что воспользовались нашими услугами. До свидания!")