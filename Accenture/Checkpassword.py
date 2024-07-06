You are given a function.
int CheckPassword(char str[], int n);
The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
str is a valid password if it satisfies the below conditions.

– At least 4 characters
– At least one numeric digit
– At Least one Capital Letter
– Must not have space or slash (/)
– Starting character must not be a number
Assumption:
Input string will not be empty.

Example:

Input 1:
aA1_67
Input 2:
a987 abC012

Output 1:
1
Output 2:
0




code:
def checkpass(a,n):
    c=0
    d=0
    if(n<4):
        return 0
    if(a[0].isdigit()):
        return 0
    for i in range(n):
        if(a[i]==' ' or a[i]=='/'):
          return 0
        if(a[i]>='A' and a[i]<='Z'):
            c=c+1
        elif(a[i].isdigit()):
            d=d+1
    if(c>0 and d>0):
        return 1
    else:
        return 0

a=input()
n=len(a)
print(checkpass(a,n))
