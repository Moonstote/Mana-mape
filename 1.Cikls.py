print("1.Uzdevums")
for i in range (1,8,1):
    print (i)

print("2.Uzdevums")
for i in range (2,19,2):
    print (i)

print("3.Uzdevums")
for i in range (7):
    print ("Sveiks!", end=" ")

print("4.Uzdevums")
print("Ievadi skaitli n")
n = int(input())
faktorials = 1
i = 0
while (i<n):
    i+=1
    faktorials = faktorials * i
    print(faktorials)


