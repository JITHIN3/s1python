l1=[]
l2=[]
print("enter the limit")
n=int(input())
print("enter the no.s:")
for i in range(0,n):
    x=float(input())
    l1.append(x)
print(l1)
for i in l1:
    if i>0:
        l2.append(i)
print(l2)

