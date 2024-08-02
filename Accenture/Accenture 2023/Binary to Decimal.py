Changing the binary input to the decimal
Input: 1010
output: 10


Code:

n=int(input())
a=str(n)
a=list(a)
a.reverse()
d=0
b=0
for i in a:
    b=b+(int(i)*pow(2,d))
    d=d+1
print(b)    
