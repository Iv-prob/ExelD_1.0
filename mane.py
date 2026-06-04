import pandas as pd


mass_nev = []
first = {}
second = {}
le = []
pr = []
name = input('Введите название файла вместе с расширением: ')
f = open(name)

# считываем данные в массив
for s in f:
    mass_nev.append(s.split(';'))
mass_nev.pop(0)

# раскидываем файл по исходным двум словарям
for i in mass_nev:
    if i[0] != '':
        first[f'{i[1]}'] = [i[2], i[0]]
    if i[4] != '':
        second[f'{i[6]}'] = [i[4], i[5]]


# начало работы
# делаем сравнения и формируем два массива для дальнейшей работы
for i in first:
    for x in second:
        if first[i][0] == second[x][0]:
            le.append(i)
            pr.append(x)

# формируем словарь, который потом будем выводить в качестве результата
# формат определяет pandas
df = pd.DataFrame({'Препарат': le,
                   'Допродажа': pr})

# записываем результаты в файл Rez.xlsx
# index=False нужно, чтобы убрать столбец с лишними номерами
df.to_excel('./Rez.xlsx', sheet_name='Результаты', index=False)


print('Всё готово!')
input("Нажмите Enter для выхода...")

print(1 + 1)
