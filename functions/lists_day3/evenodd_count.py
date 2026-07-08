nums = [12, 15, 35, 28, 42, 67, 76]
even_count = 0
odd_count = 0
for i in nums:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)