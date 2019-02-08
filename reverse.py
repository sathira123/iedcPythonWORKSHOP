i=int(input("enter the number"))
rev=0

while(i>0):
    rem=int(i%10)
    rev=rev*10+rem
    i=int(i/10)

print(rev)