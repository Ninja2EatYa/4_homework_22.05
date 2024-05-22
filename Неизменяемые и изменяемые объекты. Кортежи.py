immutable_var = 1, 2, True, 'Иван'
print(immutable_var)
immutable_var[0] = 10
print(immutable_var)  # ошибка, нельзя заменить элемент кортежа, только если элемент кортежа содержит список. Отдельные элементы списка, но не сам список, как элемент кортежа, заменить можно.

mutable_list = [4, 3, False, 'Елена']
print(mutable_list)
mutable_list[1] = 0
mutable_list[2] = True
mutable_list[3] = 'Макс'
print(mutable_list)