a = int(input("Enter a number: "))

result = []
count = a if a % 2 != 0 else a - 1

num = 1
for i in range(count):
    if num % 2 != 0:
        result.append(num)
    num += 2

print(result)
