new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

numbers = []
print(len(numbers))
numbers.append(2)
print(len(numbers))
numbers.append(200)
print(len(numbers))

nums = []
nums.extend([4, 5, 6])
print(nums)
