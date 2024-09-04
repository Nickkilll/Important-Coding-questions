A number is called happy if it leads to 1 after a sequence of steps wherein each step
number is replaced by the sum of squares of its digit that is if we start with Happy
Number and keep replacing it with digits square sum, we reach 1.
Examples:
Input:
n = 19
Output:
True
19 is Happy Number,
1^2+9^2 = 82
8^2 + 2^2 = 68
6^2+8^2 = 100
1^2 + 0^2 + 0^2 = 1
As we reached to 1, 19 is a Happy Number.
Input:
n = 20
Output:
False









code:

def check(n):
    a = 0
    c = 0
    while n > 0:
        a = n % 10
        c = c + (a * a)
        n = n // 10
    return c

n = int(input())

while n != 1 and n != 4:  
    n = check(n)

if n == 1:
    print("True")
else:
    print("False")

