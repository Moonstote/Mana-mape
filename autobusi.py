print("ievadi cilvēku skaitu")
N = int(input())
print("ievadi 1.autobusa ietilpību")
A = int(input())
print("ievadi 2.autobusa ietilpību")
B = int(input())
print("ievadi 2.autobusa ietilpību")
C = int(input())

pilni_pari = N // (A+B+C)
atlikums = N % (A+B+C)

if atlikums == 0:
    print("Jāsūta", pilni_pari, "A auto un ", pilni_pari, "B auto", pilni_pari , "C auto")
elif atlikums < A:
    print("Jāsūta", pilni_pari + 1, "A auto un ", pilni_pari, "B auto", pilni_pari , "C auto")
else:
    print("Jāsūta", pilni_pari + 1, "A auto un ", pilni_pari + 1, "B auto", pilni_pari + 1, "C auto")


