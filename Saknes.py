from math import sqrt
print("ievadi a, ievadi b, ievadi c")
a = int(input())
b = int(input())
c = int(input())
d = b*b-4*a*c
if d < 0:
    print("sakņu nav")
elif d == 0:
    print("viena sakne")
    x = -b / (2*a)
elif d > 0:
    print("divas saknes")
    x1 = -b + math.sqrt(d)
    x2 = -b - math.sqrt(d)
    print(x1,x2)