print("5.Uzdevums")
import random
skaitlis = (round(10*random.random()))
while (True):
    print("Ievadi skaitli no 1 līdz 10")
    n = int(input())
    if (n == skaitlis):
        print("Tu uzminēji!")
        break
    elif (n < skaitlis):
        print("Skaitlis ir lielāks")
    else:
        print("Skaitlsi ir mazaks")

