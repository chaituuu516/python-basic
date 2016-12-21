#% calculator#
print ("1.regular")
print ("2.L.E")
c=int(input())
if(c==1):
    print ("enter total marks to calculate your % :")
    a = int(input())
    b = float((a*100/4500))
    print (b,"%")
if(c==2):
    print ("enter total marks to calculate your % :")
    a = int(input())
    b = float((a*100/3100))
    print (b,"%")
if(c>2):
    print ("choose correct option ")
