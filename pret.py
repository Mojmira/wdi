a=str(input("podaj slowo: "))
n=int(input("podaj przesuniecie: "))
b=[]


def cezar(a,b,n):
    l=len(a)
    for i in range(0,l):
        b.append(chr((ord(a[i])+n-97)%26+97))
    print(b)


def brutus(a,b,n):
    l=len(a)
    for i in range(0,l):
        b.append(chr((ord(a[i])-n-97)%26+97))
    print(b)
brutus(a,b,n)