#5532_방학숙제
l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())

kor = a // c
if a%c > 0:
    kor += 1
math = b // d
if b%d > 0:
    math += 1

print(l - max(kor, math))
