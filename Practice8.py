a=int(input())
p=0
q=1
print("Fibonacci series:", p,q,end=" ")
for i in range(0,a+1):
    r=p+q
    print(r,end=" ")
    p=q
    q=