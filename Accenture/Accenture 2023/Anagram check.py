Annagram code:



def are_anagrams(a, b):
    if sorted(a) == sorted(b):
        return 1
    else:
        return 0

# Example usage
a=input()
b=input()
r=are_anagrams(a,b) 
if(r):
    print("Anagram")
else:
    print("No anagram")
    
