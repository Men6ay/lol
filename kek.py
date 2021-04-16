# def a(b):
#     def c():
#         print('Я - декоратор')
#         b()
#     return c

# def d():
#     print('Я все сделал')
# a = a(d)
# a()



# def dekortar(dek):
#     temperatur = int(input('Enter: '))
#     def a():
#         try:
#             if temperatur > 10:
#                 dek()
#                 return('“На улице тепло, давай погуляем, я не против!”.')
#             elif temperatur > 0 and temperatur < 10:
#                 dek()
#                 return('“Прохладно. Надо одеться!”,')
#             elif temperatur > -10 and temperatur < 0:
#                 return('“Холодно. Потеплее оденься и пойдем!”,')
#             elif temperatur < -10:
#                 return('“Мороз. Лучше давай дома посидим, фильм посмотрим!”')
#         except:
#             return("oshibka")
#     return a


# def go_for_a_walk():
#     print('“Давай, пойдем погуляем на улице!”')
# l = dekortar(go_for_a_walk)
# print(l())