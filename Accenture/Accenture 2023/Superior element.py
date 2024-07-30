Find the superior elements
Input: 6 
       7 9 5 2 8 7
Output: 3

Explanation:
9 8 and 7 is greater than number that to it's left



n = int(input())
a = list(map(int, input().split()))
e = 0

for i in range(n):
    sup = 1
    for j in range(i+1,n):
        if a[i] <= a[j]:
            sup=sup-1
            break
    if sup==1:
        e += 1

print(e)
