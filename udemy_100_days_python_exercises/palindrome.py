word= "abcddcba"


n=len(word)
i=n-1
ls = []

while i != -1:
    ls.append(word[i])
    i -=1

reversed_word="".join(ls)

if reversed_word==word :
    print("This is a palindrome.")

else:
    print("This is not a palindrome.")