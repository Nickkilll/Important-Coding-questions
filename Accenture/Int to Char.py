Input
n: 12
num: 718

Output
4BA

Explanation
num       Divisor       quotient       remainder
718           12               59                 10(A)
59             12                4                   11(B)
4               12                0                   4(4)

Sample Input
n: 21
num: 5678

Sample Output
CI8




CODE:

n=int(input())
num=int(input())
rem=[]
out=[]
a=num
while(a!=0):
    b=a%n
    rem.append(b)
    a=a//n
for x in rem:
    if(x>9):
        x=x-10
        out.append(chr(x+ord('A')))
    else:
        out.append(str(x))
        
out.reverse()
for i in out:
    print(i,end="")
    
