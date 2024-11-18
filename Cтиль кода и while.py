# name = input("Enter your name")
# if 5 > 1:
#     print("ok")
#     if 1 > 0:
#         print("zncik") # CTRL + ALT + L = Отформатированный текст по отступам


# while 1 > 0:
#     number = int(input("Введите число :"))
#
#     if number % 2 == 0:
#         print('Число четное')
#         continue
#     else:
#         print("Число нечетное")
#     print(2636)
#
# print("Я за циклом")


# Все что выше это по лекции, ниже домашнее задание


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ploas_number = []
index = 0
list_len = len(my_list)
noll = my_list[4]


while index < list_len :
    if my_list[index] < 0:
        break
    ploas_number.append(my_list[index])
    index += 1
print(ploas_number)



for num in ploas_number:
    if num == 0:
        continue
    print(num)




