# print("Hello World!")

#演算

# print(1+1)
# print(1-1)
# print(1*1)
# print(10/2)
# print(5%3)

#変数

# hoge = 's_size'
# hoge_length = 0
# hoge_times = 5.5

# if hoge_length > 6:
#     print('ooi')
# elif hoge_length == 0:
#     print('nai!')
# else :
#     print('sukunai')

# 関数

# def unko_funbaru(arg):
#     unko_status = arg
#     if(unko_status < 10):
#         return 'mada daijoubu'
#     else: 
#         return 'yabai'

# print(unko_funbaru(12))

# list

# unko_list = ['unko_small', 'unko_medium', 'unko_large']
# print(unko_list[0])

# for文

# for index in range(3):
#     print(unko_funbaru(11))

# for item in unko_list:
    # print(item)

#with
# open()

# with open('./dummy.txt', 'r') as file:
#     print(file.read())


# class

# class Card:
#     def __init__(self, date, user_name):
#         self.date = date
#         self.user_name = user_name
#     def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

# date_a = '2024-09-03'
# user_name_a = 'Taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2024-09-04'
# user_name_b = 'Kayoko'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())


# import

import numpy
numpy_list = [3, 1, 5, 1, 10, 209, 500]
print(numpy.sum(numpy_list))