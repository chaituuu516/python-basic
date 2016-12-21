#armstrong
def arm(n):
    a = n
    s = 0
    while (n!=0):
        r = n%10
        s = s+(r*r*r)
        n = n//10
    if(s==a):
        print (s)
    return
print ("enter a num")
n=int(input())
for i in range(2,n+1):
    arm(i)
