Armstrong number with the factorial form

Input : 145
1!+4!+5!=145

if 145== 145
true is output

code:
n=int(input())
a=list(str(n))
b=len(a)
c=1
d=0
for i in range(b):
    for j in range(1,int(a[i])):
        c=c*j
    d=d+c 
    c=1
print(d)
