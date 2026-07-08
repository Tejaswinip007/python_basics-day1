nums = [12, 45, 36, 35, 86, 26]
largest = nums[0]
second_largest = nums[0]
for i in nums:
    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest and i != largest:
        second_largest = i
print(largest)
print(second_largest)
    