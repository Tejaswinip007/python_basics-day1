num = 12321
rev = 0
org = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if org == rev:
    print("palindrome")
else:
    print("not a palindrome")