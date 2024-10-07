#question = input('Milyen napja volt?')
#question_lowercase = question.lower()
#if question_lowercase == 'igen':
#    print('Csodálatos!')
#elif question_lowercase == 'nem':
#   print('Holnap jobb lesz!')
#else:
#    print('Sajnos nem értem a válaszodat!')

"""2. Feladat
Készíts egy programot, ami bekér egy számot a felhasználótól, majd kiírja, hogy a megadott szám páros-e vagy páratlan!

[Tipp] A maradékos osztás segít! Mennyivel is kell elosztanod a számot maradékosan, hogy kiderüljön páros-e? Ebben az esetben mennyi lesz a maradék?
"""
#
#szam= int(input('Adj meg egy számot'))
#if szam  % 2 == 0:
#    print('A megadott szám páros')
#else:
#    print('A megadott szám páratlan ')

"""3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb."""

import random
random_number = random.randint(a=1, b=5)
number = input("Gondoltam egy számra")
print(f"Erre gondoltam: {random_number}")
if  random_number == number:
    print("Eltaláltad!")
else:
    print("Nem talált")


