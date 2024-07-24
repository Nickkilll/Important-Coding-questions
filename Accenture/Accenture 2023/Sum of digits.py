You are required to implement the following function:
int DifferenceSumofDigits (int* arr, int n);
The function accepts an array arr of n positive integers as its argument. Let's suppose
Sum of digits of an integer f(x)
You are required to calculate the value of following:
F1= [f(arr[0])+f(arr[1])+ f(arr[2]) + ...f(arr[n-1])] %10
F2 = [(arr[0] + arr[1] + arr[2] + ... +arr[n-1])]%10.
F=F1-F2
and return the value of F.
Note: n > 0
Example:
Input:
arr: 11 14 16 10 9 8 24 5 43
n: 10
Output:
-4
Explanation:
The value of F, is (1 + 1) +(1+4)+(1+6) (1+0) + (9) + (8)
(2+4)+(5)+(4)+3 equal to 50 and 50%10=0 and the value of 11+14+16+10+9+8+24+ 5+4+3
which is equal to 104 and (104%10)=4 So , F=0-4=-4
(The first line represents "n", the second line represents the elements of the array arr)
Sample input
Input:
Arr: 16 18 20
n: 3
Sample Output
4


CODE:

n= int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    b += sum(int(j) for j in str(i))
d = b % 10
f=sum(a)
e= f % 10
# print(d-e)
print(d-e)




