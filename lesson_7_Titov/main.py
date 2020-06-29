str= input()
l=len(str)
for i in range (l//2):
    if str[i] != str [-1-i]:
        print('Its not palindrome')
        quit()
print('Its palindrome')