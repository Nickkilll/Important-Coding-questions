Files sum
input 1 : size of the array
input 2 : file_1  file_2 file_3 file_4
output: 3
Max should be printed




code:


n=int(input())
a=list(map(str,input().split()))
b=[]
for i in a:
    c=i.split('_')
    if(len(c)==2 and c[1].isdigit() and c[0]=='file'):
        b.append(c[1])
print(max(b))   
