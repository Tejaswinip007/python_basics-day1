nums = [8, 3, 134, 2, 1230]
largest = nums[0]
for i in nums:
    if i > largest:
        largest = i
print(largest)