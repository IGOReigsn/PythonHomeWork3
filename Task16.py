"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1"""


n=int(input("Количество элементов в массиве: ")) 
if n>0:
    a=[]
    for i in range (n):
        a.append(int(input("Введите элемент массива: ")))
    x=int(input("Число Х: "))
    print("Количество чисел ", x, " в массиве = ", a.count(x)) 
else: print("Количество элементов в массиве должно быть положительным ")