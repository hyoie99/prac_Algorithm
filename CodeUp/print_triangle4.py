num = int(input())

for n in range(1, num+1):
    print("*" * n)
for n in range(num-1, 0, -1):
    print("*" * n)