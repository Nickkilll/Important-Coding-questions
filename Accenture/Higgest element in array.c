To get an array and print it's heighest value and it's index position



#include<stdio.h>
int main()
{
    int n,c=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    
    for(int i=0;i<n;i++)
    {
        c=0;
        for(int j=0;j<n;j++)
        {
            if(arr[i]>=arr[j])
            {
                c++;
            }
        }
        if(c>=n)
        {
            printf("%d \n%d",arr[i],i);
            break;
        }
    }
}
