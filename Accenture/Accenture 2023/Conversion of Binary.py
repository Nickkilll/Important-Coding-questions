Convert Decimal to Binary 
You are given an integer 'n'

. Write a Python function to calculate and

return the sum of the digits in 'n' after converting it to its binary
representation.

For example, 15, which has a binary representation of 1111, should
return 4.





CODE:

n=int(input())
a=n
c=[]
while(a!=0):
    b=a%2
    c.append(b)
    a=a//2
c.reverse()
print(sum(c))
    
