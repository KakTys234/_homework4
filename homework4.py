# Пункт 2
immutable_var = 1, 3, False, 'Матрица', 'System'
print(immutable_var)
# Пункт 3
# print(immutable_var[3])
# immutable_var[3] = 'off'
# print(immutable_var)
# Изменить элементы кортежа нельзя, потому что кортеж не поддерживает обращение к элементам, т.е. они неизменяемые.
# Если внутри кортежа есть элемент ввиде списка, то элементы самого списка менять можно.
# Например:
name = ([3, 0, 5], 5, 6, 7)
print(name)
#меняем
name[0][1] = 4
# получим
print(name)
# Пункт 4
mutable_list =['A', 1, 25, 'matrix']
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list[3] = 'sport'
print(mutable_list)
mutable_list.extend(['boll'])
print(mutable_list)
