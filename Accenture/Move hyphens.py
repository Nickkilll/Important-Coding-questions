Example :-

Input:
str.Move-Hyphens-to-Front
Output:
—MoveHyphenstoFront
Explanation:-

The string “Move-Hyphens -to-front” has 3 hyphens (-), which are moved to the front of the string, this output is “— MoveHyphen”

Sample Input

Str: String-Compare
Sample Output-

-StringCompare


CODE:
n=input()
fin=""
c=0
for x in n:
    if(x=='-'):
        c=c+1
    else:
        fin=fin+x
print('-'*c+fin)        
