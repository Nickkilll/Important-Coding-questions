Longest string in the sentence
input:
I am a good bot
output: 
good




CODE:


n=input()
s=n.split()
m=""
for i in s:
    c=i
    if len(c)>len(m):
        m=c
print(m)  
