import csv

def add_info(file):
    last_name = input('Введите фамилию ученика: ').capitalize()
    first_name = input('Введите имя ученика: ').capitalize()
    num_class = input('Введите класс ученика: ').lower()
    with open(file, 'a', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                'Биология', 'Химия', 'История', 'География', 'Физика']
        writer = csv.DictWriter(data, fieldnames= fields)
        writer.writerow({'Фамилия': last_name, 'Имя': first_name, 'Класс': num_class})

        
def add_grades(file):
    subject = input('Введите название предмета: ').capitalize()
    grade = input('Введите оценку: ')
    number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
    my_dict = []
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        for row in csv.reader(data):
            my_dict.append({'Фамилия': row[0], 'Имя': row[1], 'Класс': row[2], 'Литература': row[3], 'Русский язык': row[4], 'Математика': row[5],\
                      'Физкультура': row[6], 'Информатика': row[7], 'Иностранный язык': row[8], 'Биология': row[9], 'Химия': row[10], 'История': row[11],\
                          'География': row[12], 'Физика': row[13]})
    my_dict[number][subject] += f'{grade} '
    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                'Биология', 'Химия', 'История', 'География', 'Физика']
        writer = csv.DictWriter(data, fieldnames= fields)
        writer.writerows(my_dict)
    

def change_info(file):
    print('Введите цифру, соответствующую типу информации, которую нужно изменить:')
    type_info = int(input('1 - фамилия\n2 - имя\n3 - класс\n'))
    column = ''
    if type_info == 1:
        column = 'Фамилия'
    elif type_info == 2:
        column = 'Имя'
    else:
        column = 'Класс'
    number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
    my_dict = []
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        for row in csv.reader(data):
            my_dict.append({'Фамилия': row[0], 'Имя': row[1], 'Класс': row[2], 'Литература': row[3], 'Русский язык': row[4], 'Математика': row[5],\
                      'Физкультура': row[6], 'Информатика': row[7], 'Иностранный язык': row[8], 'Биология': row[9], 'Химия': row[10], 'История': row[11],\
                          'География': row[12], 'Физика': row[13]})
    new_info = input('Введите новую информацию: ')
    my_dict[number][column] = new_info
    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                'Биология', 'Химия', 'История', 'География', 'Физика']
        writer = csv.DictWriter(data, fieldnames= fields)
        writer.writerows(my_dict)