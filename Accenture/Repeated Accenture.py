Repeated Accenture:

input: 
2
{name,file}

output:
fn



n=int(input())
a=[]
s=""
for i in range(n):
    a.append(input())
for i in range(n):
    c=a[i][0]
    s=s+c
print(''.join(sorted(s)))
