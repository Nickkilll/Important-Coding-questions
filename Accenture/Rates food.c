Problem Description :
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
Output:

4

Explanation:
Total amount of food required for all rats = r * unit

= 7 * 2 = 14.

The amount of food in 1st houses = 2+8+3+5 = 18. Since, amount of food in 1st 4 houses is sufficient for all the rats. Thus, output is 4






















code:


#include<stdio.h>
int check(int rate, int *arr ,int n)
{
    int c=1,d=0;
        if(n==0)
        {
            return -1;
        }
        
    for(int i=0;i<n;i++)
    {
        d+=arr[i];
        if(d>=rate)
        {
            return c;
        }
        c++;
        
        if(d<rate)
        {
            return 0;
        }
        
    }
}

int main()
{
    int r,u,n;
    scanf("%d %d %d",&r,&u,&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    int rate= r*u;
    printf("%d",check(rate,arr,n));
}
