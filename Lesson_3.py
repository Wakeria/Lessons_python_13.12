# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.
# from random import sample

# def num_find (len_list, number):
#     new_list = sample (range(1, len_list *2), k=len_list)
#     print(new_list)
#     if number in new_list:
#         return 'Yes'
#     return 'No'    
# print(num_find(int(input('введите длину списка: ')), int (input('введите число: '))))    


# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

# from random import sample
# def spisok (count, word = 'abs'):
#     my_list = []
#     for i in range(count):
#         temp = sample(word, k=3)
#         my_list.append("".join(temp))
#     return my_list  

# def index_find (word_2, list_2):
#     if word_2  in list_2 and list_2.count(word_2) > 0:
#         index_1 = list_2.index (word_2)
#         print (list_2.index (word_2, index_1+1))
#     else:
#         print(-1)    

# List_1 = spisok(int(input('введите число: ')))
# print (List_1)  
# index_find (input(), List_1)

