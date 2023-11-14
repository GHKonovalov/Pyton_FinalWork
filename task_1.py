# # 6 -> 1  4  1
# # 24 -> 4  16  4
# # 60 -> 10  40  10



# t = input('Введите номер билета: ')
# l = int(t[0]) + int(t[1]) + int(t[2])
# r = int(t[3]) + int(t[4]) + int(t[5])
# if l == r:
#     print('Yes')
# else:
#     print('NO')
# # или
# s = input('Введите 6-значный номер билета: ')
# if len(s) != 6:
#     print(f'Число {s} не 6-ти значное')
# else:
#     res1 = 0
#     res2 = 0
#     for i in range(len(s)//2):
#         res1 += int(s[i])
#         res2 += int(s[len(s)//2 + i])
#     if res1 == res2:
#         print(f'{s} счастливый номер')
#     else:
#         print(f'{s} не счастливый номер')

# n = 385916
# n = int(input())



a,b,c = int(input('В-те 1-ю сторону: ')),int(input('В-те 2-ю сторону: ')),int(input('В-те кол-во долек: '))
if c%a == 0 or c%b == 0:
    print('Yes')
else: print('No') 