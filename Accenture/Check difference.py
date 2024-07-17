You are given a function,
int findCount(int arr[], int length, int num, int diff);

The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

Example:
Input:

arr: 12 3 14 56 77 13
num: 13
diff: 2
Output:
3

Explanation:
Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14.



Code:

def diff(a,num,dif):
    c=0
    for x in a:
        if(abs(x-num)<=dif):
            c=c+1
    if(c==0):
        return -1
    return c


n=int(input())
a=[int(input()) for _ in range(n)]
num=int(input())
dif=int(input())
print(diff(a,num,dif))
