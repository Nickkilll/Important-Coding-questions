Rate food:

The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

Note:

Return -1 if the array is null
Return 0 if the total amount of food from all houses is not sufficient for all the rats.
Computed values lie within the integer range.
Example:

Input:

r: 7
unit: 2
n: 8
arr: 2 8 3 5 7 4 1 2

Output is 4

Explaining it
7*2=14
Now in the array
2+8+3+5 will enough to feed the rate that is Greater dhan 14
Hence it should print 4


code in python:

def rats_can_eat(food,n,a):
    d=0
    c=1
    
    if(n==0):
        return -1
    for i in range(n):
        d=d+a[i]
        if(d<=food):
           c=c+1
    return c

r=int(input())
u=int(input())
food=r*u
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
c=rats_can_eat(food,n,a)
print(c)
    
