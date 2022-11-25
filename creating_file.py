import csv

def creating(file):
    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика', 'Иностранный язык',\
                'Биология', 'Химия', 'История', 'География', 'Физика']
        writer = csv.DictWriter(data, fieldnames=fields)
        writer.writeheader()