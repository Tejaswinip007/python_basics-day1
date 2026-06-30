num = 153
org = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** 3
    num = num // 10
if org == sum:
    print("Armstrong number")
else:
    print("not a armstrong number")