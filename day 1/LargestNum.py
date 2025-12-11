a=int(input("enter a:",))
b=int(input("enter b:",))
c=int(input("enter c:",))

if a>=b and a>=c:
    print(a,"is the largest number")
elif b>=c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")        