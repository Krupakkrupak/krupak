numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

output = {}

for i in range(1, 10):
    count = 0
    for n in numbers:
        if n % i == 0:
            count += 1
    output[i] = count

print(output)
