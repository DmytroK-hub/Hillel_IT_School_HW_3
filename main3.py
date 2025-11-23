my_list = [2, 32, 1, 9, 0, 2, 7, 21, 4]

size = len(my_list)

if size % 2 != 0:
    middle = (size +1) // 2
    print(my_list, "не парне")
else:
    middle = size // 2
    print(my_list, "парне")

lst1 = my_list[:middle]
lst2 = my_list[middle:]
lst3 = [lst1, lst2]

print("Перша половина: ", lst1)
print("Друга половина: ", lst2)
print("Результат програми ", lst3)


# my_list = [2, 32, 1, 9, 0, 2, 7, 21]
#
# x = int(input("Введіть число(індех) від якого почнеться розділ списку: "))
#
# lst1 = my_list[:x]
# lst2 = my_list[x:]
#
# print(lst1)
# print(lst2)
# print(f"{[lst1]}, {[lst2]}")