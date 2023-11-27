# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells\
#  that she sells are sea shells I'm sure. So if she sells sea\
#  shells on the sea shore I'm sure that the shells are sea\
#  shore shells"

# words = text.lower().replace('.', ' ').split()

# st = set(words)

# print(len(st))

# print(len(set(words)))

list_1 = [1, 2, 8, 8, 2, 2, 4, 5, 10, 9, 9, 5,]
k = 3
count_k = 0
for i in list_1:
    if i == k:
        count_k += 1
print(count_k)