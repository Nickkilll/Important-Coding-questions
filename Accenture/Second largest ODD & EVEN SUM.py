def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

All array elements are unique
Treat the 0th position as even
NOTE

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input

arr:3 2 1 7 5 4

Output

7

Explanation

Second largest among even position elements(1 3 5) is 3
Second smallest among odd position element is 4
Thus output is 3+4 = 7
Sample Input

arr:1 8 0 2 3 5 6

Sample Output

8




CODE:

def diff(n,a,even,odd):
    if n==0:
        return 0
    if n<=3:
        return 0
    for i in range(n):
        if(i%2==0):
            even.append(a[i])
        else:
            odd.append(a[i])
    even1=sorted(even)
    odd1=sorted(odd)
    return (even1[len(even1)-2]+odd1[len(odd1)-2])

n=int(input())
a=[int(input()) for _ in range(n)]
even=[]
odd=[]
print(diff(n,a,even,odd))
