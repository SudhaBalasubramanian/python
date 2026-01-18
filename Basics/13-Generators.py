def square_numbers(num):
    for i in num:
        yield i * i

nums = square_numbers([1,2,3,4,5])
print(nums)

for num in nums:
    print(num)