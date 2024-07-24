You are required to implement the following function:
int ReArrangeArray( int arr, int len); The function accepts an array 'arr' of length 'len' as
its argument. You are required to re-arrange the elements : positive integers are on right,
but retaining their order of appearance as in the original array. Return the modified
array.
Note:
All operations are to be performed in-place i.e. you cannot use another array.
If 'arr' is NULL (None, in case of Python), then return NULL.
Assumption: Consider 0 as positive number.
Example:
Input: arr: 1 7-5 9-12 15
Output:
-5 -12 1 7 9 15
Explanation:
Re-arranging the elements of array {1, 7, -5, 9, -12, 15) such that negative integers are on
left and positive integers are (1,7, 9, 15) at the right.
Sample input
arr: -6 10 8 -5 -14 -17 23 -20 -18 -19
Sample Output
-6-5-14 -17 -20 -18 -19 10 8 23
Instructions.
This is a template based question, DO NOT write the "main" function. Your code is judged
by an automated system, do not write any additional
Welcome greeting message







CODE:

n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
        if i<0:
            b.append(i)
        else:
            c.append(i)
e=b+c            
for i in e:
    print(i,end=" ")
