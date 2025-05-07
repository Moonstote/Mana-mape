print("5.Uzdevums")
import random
slepenais = (random.randint(1,10))
gajienu_skaits = 0
max_minējumu_skaits = 5
print("Jūs drikstat minēt piecas reizes")
while (True):
    if max_minējumu_skaits == gajienu_skaits:
        print("Tu esi iztērējis visus minējumus! Beigas!")
        break
    print("Ievadi skaitli no 1 līdz 10")
    skaitlis = int(input())
    gajienu_skaits +=1
if skaitlis == slepenais:
        print("Tu uzminēji!", gajienu_skaits, "gājienos")
if skaitlis < slepenais:
        print("Skatilis ir lielāks")
if skaitlis > slepenais:
        print("Skaitlis ir mazāks")
