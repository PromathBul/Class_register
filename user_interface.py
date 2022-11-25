from add_info import add_info, add_grades
from check import check_exist
from add_info import change_info
from search import search_word, search_grades

def menu():
    flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    while flag == '0':
        check_exist()
        print('Введите цифру, соответствующую правам доступа:')
        flag = input('1 - учитель\n2 - ученик\n')

        while flag != '1' and flag != '2':
            print('Введите цифру, соответствующую правам доступа:')
            flag = input('1 - учитель\n2 - ученик\n')

        if flag == '1':
            print('Введите цифру, соответствующую действию: ')
            choice = int(input('1 - ввести данные об ученике\n2 - изменить данные\n3 - внести оценки\n4 - поиск информации\n'))
            while choice < 1 or choice > 4:
                print('Введите цифру, соответствующую действию: ')
                choice = int(input('1 - ввести данные об ученике\n2 - изменить данные\n3 - внести оценки\n4 - поиск информации\n'))
            
            if choice == 1:
                add_info('pupils.csv')
            elif choice == 2:
                last_name = input('Введите фамилию ученика, информацию о котором хотите изменить: ')
                search_word(last_name)
                change_info('pupils.csv')
            elif choice == 3:
                last_name = input('Введите фамилию ученика, которому Вы хотите выставить оценку: ')
                search_word(last_name)
                add_grades('pupils.csv')
            elif choice == 4:
                last_name = input('Введите фамилию ученика: ')
                search_word(last_name)
                search_grades()
        else:
            last_name = input('Введите свою фамилию: ')
            search_word(last_name)
            search_grades()
        flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    print('Программа завершена.')

