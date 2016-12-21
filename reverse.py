print ("enter a number to reverse")
a = int(input())
s=0
r=0
while(a!=0):
    r=a%10
    s=s*10+r
    a=a//10
print ("reverse is",s)
