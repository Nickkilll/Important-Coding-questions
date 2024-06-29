Problem statement

7 types of Indian currency notes are given, ie, Re. 1, Rs. 2. Rs. 5, Rs10, Rs 20, Rs 50 and Rs 100.

You are required to implement the following function

int MinNumberOfNotes (int n);

The function accepts an integer 'n' as its argument. Implement the function to find and return the minimum number of notes required to form the amount 'n'.

Assumption

n>=0

Note 

Return 0,if n=0
multiple notes of the same type can be used
Input format :
Input integer is the value of n.

Output format :
Output integer is the number of notes required.

Sample test cases :
Input 1 :
175
Output 1 :
4
Input 2 :
84
Output 2 :
5






Ouput:


#include<stdio.h>
// int MinNumberofNotes(int a)
// {
//     int c=0;
//     for(int i=0;i<n;i++)
//     {
        
//     }
    
// }


int main()
{
    int n,c=0;
    scanf("%d",&n);
    int a[7]={100,50,20,10,5,2,1};
    for(int i=0;i<8;i++)
    {
        while(n>=a[i] && n>0)
        {
            n=n-a[i];
            c++;
        }
    }
    printf("%d",c);
    // int c=MinNumberOfNotes(a);
}
