def Palindrome(str):

    for i in range(0, int(len(str) / 2)): #half string
        if str[i] != str[len(str) - i - 1]: #if 1st half doesnt equal 2nd half
            return False #not palindrome
    return True

word = "noon"
answer = Palindrome(word.upper()) #pass in string, account for letter case

if (answer):
    print("Yes")
else:
    print("No")
