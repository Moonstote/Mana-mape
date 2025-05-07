print("Ievadi skaitli 1")
A = int(input())
print("Ievadi skaitli 2")
B = int(input())
if B == 0:
    print("Skaitlis ir 0")
else:
    skaitlis = A // B
    print(skaitlis)
    atlikums = A % B
    print(atlikums)
