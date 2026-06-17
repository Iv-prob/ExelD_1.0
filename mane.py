import pandas as pd


problem_count = 0
problem_l = []
flag = True
unique_name = set()
mass_nev = []
first = []
second = []
le = []
pr = []
pr_2 = []
# name = input('Введите название файла вместе с расширением: ')
name = "Допродажа для обработки_t.csv"
f = open(name)

# считываем данные в массив
# mass_nev = [['ЦБ-00123415', 'Навтекс салфетки марл.стер. 16х14 №20', 'Салфетки стерильные', '', 'Витамин Д3',
# 'ЦБ-00037072', 'Эсслиал Форте капс 300мг №30\n'], ['ЦБ-00191219', '1Вин 3МА/В6 капс. №90', 'Поливитамины', '',
# 'Витамин Д3', 'РТ-00002042', 'Витамир Магний + В6 форте таб. №30\n'], ...] - массив из строк
for s in f:
    mass_nev.append(s.split(';'))
mass_nev.pop(0)

# раскидываем файл по исходным двум словарям
# first = [['Навтекс салфетки марл.стер. 16х14 №20', 'Салфетки стерильные', 'ЦБ-00123415', '2'],
# ['1Вин 3МА/В6 капс. №90', 'Поливитамины', 'ЦБ-00191219', '3'], ...]
# second = [['Эсслиал Форте капс 300мг №30\n', 'Витамин Д3', 'ЦБ-00037072', '2'],
# ['Витамир Магний + В6 форте таб. №30\n', 'Витамин Д3', 'РТ-00002042', '3'], ...]
n = 2
for i in mass_nev:
    if i[1] != '' and i[1] not in unique_name:
        first.append([i[1].strip(), i[2].strip(), i[0].strip(), str(n)])
        unique_name.add(i[1])
    if i[4] != '':
        second.append([i[6].strip(), i[4].strip(), i[5].strip(), str(n)])
    n += 1


# начало работы
# делаем сравнения и формируем два массива для дальнейшей работы
for i in first:
    for x in second:
        if i[1] == x[1]:
            le.append(i[0])
            pr.append(x[0])
            pr_2.append((i[1]))
            flag = False
    if flag:
        problem_l.append(i)
        problem_count += 1
    flag = True

# формируем словарь, который потом будем выводить в качестве результата
# формат определяет pandas
df = pd.DataFrame({'Препарат': le,
                   'Допродажа': pr,
                   'Категория': pr_2})

# записываем результаты в файл Rez.xlsx
# index=False нужно, чтобы убрать столбец с лишними номерами
df.to_excel('./Rez.xlsx', sheet_name='Результаты', index=False)

if problem_count > 0:
    print(f'Препаратов, которым не нашлось допродаж {problem_count}:')
    for problem_position in problem_l:
        print(f'Строка {problem_position[3]}, наименование: "{problem_position[0]}" категория: "{problem_position[1]}"'
              f' код: {problem_position[2]}')
else:
    print('Каждому препарату нашлась минимум одна допродажа')
print('')

print('Всё готово!')
input("Нажмите Enter для выхода...")
