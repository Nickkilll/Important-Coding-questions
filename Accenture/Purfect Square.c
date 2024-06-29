To get a sqaure u need as sides to be equal

#include<stdio.h>
#include<math.h>
int main()
{
    int n,count=0;
    scanf("%d",&n);
    int arr[n],arr1[n];
    
    //get array elemets
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    
    //assign square root in another array 
    for(int i=0;i<n;i++)
    {
        arr1[i]=sqrt(arr[i]);
    }
    
    //check
    for(int i=0;i<n;i++)
    {
        if(arr1[i]*arr1[i]==arr[i])
        {
            count++;
        }
        else
        {
            continue;
        }
    }
    printf("%d",count);
}
