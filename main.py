import random

#lst = 'ΣΟΚΟΦΡΕΤΑ'
#print(random.choice(lst))

with open('kremala_lexeis.txt', 'r', encoding='utf8') as f:
    word = random.choice(f.readlines()).rstrip()


print(word)

print('-'*len(word))

max_wrong_tries = 3

b = True
tries = 0

while b:

    letter = input('Μάντεψε Γράμμα:')

    if letter in word:
        print('Μάντεψες σωστά!!!')
    else:
        print('Δεν βρέθηκε αυτό το γράμμα!!!d')
        tries += 1

    if tries == max_wrong_tries:
        b = False
