You are required to implement the following function

int* MoveZerosToEnd(int*	arr,	int	n); 

The	function	takes	an	integer	array	and	its	length	as	input.	Implement	the	function	to	modify	the	array such	that	all	the	0’s	are	moved	to	the	end	of	the	array.  

Input format :
The first input integer is the size of the array.

The next line of integers is the array elements.

Output format :
The output is the modified array with all zeros moved to the right side.

Sample test cases :
Input 1 :
10
1 9 8 4 0 3 0 7 9 0
Output 1 :
1 9 8 4 3 7 9 0 0 0 
Input 2 :
8
1 2 0 3 2 0 9 0
Output 2 :
1 2 3 2 9 0 0 0 






Code:

#include<stdio.h>
int* MoveZeros(int *arr,int n )
{
    int temp=0;
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            
           if(arr[i]==0)
             {
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
             }
        }
    }
    return arr;
    
    // for(int i=0;i<n;i++)
    // {
    //     printf("%d ",arr[i]);
    // }
    
}





int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    MoveZeros(arr,n);
    
    for(int i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    
}
