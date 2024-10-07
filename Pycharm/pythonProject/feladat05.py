"""1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

# import random
#
# # Véletlenszám generálása 1 és 3 között
# random_number = random.randint(1, 3)
#
# # Felhasználói szám bekérése
# user_number = int(input("Adj meg egy számot 1 és 3 között: "))
#
# # Összehasonlítás
# if user_number < 1 or user_number > 3:
#     print("A megadott szám nem esik az 1-3 tartományba.")
# elif random_number == user_number:
#     print(f"Talált! A generált szám is {random_number} volt.")
# else:
#     print(f"Nem talált. A generált szám {random_number} volt, a te számod pedig {user_number}.")



"""A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!"""

import random

# Felhasználó választása
user_choice = input("Fej vagy írás? (írj 'fej'-et vagy 'írás'-t): ").lower()

# Pénzfeldobás szimuláció (fej = 0, írás = 1)
coin_flip = random.choice(['fej', 'írás'])

# Eredmény kiírása
if user_choice not in ['fej', 'írás']:
    print("Érvénytelen választás. Kérlek, csak 'fej'-et vagy 'írás'-t adj meg.")
elif user_choice == coin_flip:
    print(f"Gratulálok, eltaláltad! A pénzfeldobás eredménye: {coin_flip}.")
else:
    print(f"Sajnos nem találtad el. A pénzfeldobás eredménye: {coin_flip}.")
