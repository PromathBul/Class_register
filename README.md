Программа представляет собой информационную систему по выставлению оценок ученикам (примитивный электронный дневник).

Интерфейс разделен на два вида пользователей:
- __учитель__; ему доступно четыре функции:
    - *ввод данных об ученике* (фамилия, имя, класс)
    - *изменение этих данных*    
    - *внесение оценок*
    - *просмотр успеваемости учеников по всем предметам или по конкретному*
- __ученик__
    - ученику доступна только функция *просмотра успеваемости учеников*, как своей так и других

Поиск производится по фамилии.

Ситуация возможного существования однофамильцев разрешена запросом порядкового номера интересующего ученика, который выводится в консоль вместе с фамилией, именем и номером класса.

Все внесенные данные и изменения сохраняются в файле с расширением `.csv`. Поэтому при желании его можно просматривать через MS Excel или аналогичные программы.