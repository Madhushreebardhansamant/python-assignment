# 5)Write a function given string is a palindrome or not without using for loop
def isPalindrome(input):
    if (input == input[::-1]):
        return True
    return False
input = "cuattauc"
result = isPalindrome(input)
if result:
    print("yes,isPalindrome")
else:
    print("No,notPalindrome")

# or

pal = lambda x: True if ''.join(x[::-1]) == x else False
print(pal('malayalam'))