lst = [10, 68, 38, 45, 96, 38]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)