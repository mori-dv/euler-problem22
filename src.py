import string
alphabet = list(string.ascii_uppercase)
names = open("p022_names.txt","r")

lst = list()
names_list = list()
for name in names:
    lst += name.split(',')
for i in lst:
    if (i not in names_list):
        names_list.append(i)
names_list = sorted(names_list)

total_score = 0
for word in names_list:
    sum = 0
    score = 1
    for harf in word:
        for alephba in alphabet:
            if (harf == alephba):
                sum += alphabet.index(alephba)
    score = sum * (names_list.index(word) + 1)    
    total_score += score

print('the total score of all names in the given list is %i ' % total_score)
