Encode the Number:

You work in the message encoding department of a national security
message agency. Every message that is sent from or received in your
office is encoded. You have an integer N and each digit of N is squared
and the squares are concatenated together to encode the original
number. Your task is to find and return an integer value representing
the encoded value of the number.

Input Specification:
input1: An integer value N representing the number to be encoded.

Output Specification:
Return an integer value representing the encoded value of the number.
Example 1:
input1: 34

Output: 916

Explanation:
Here, the given integer is 34, and the square its digit are:
3^2= 9
42=16




Code:

n=int(input())
n=list(str(n))
b=[]
for i in n:
    c=int(i)*int(i)
    b.append(c)
for i in b:
    print(i,end='')
