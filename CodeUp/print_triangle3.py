num = int(input())

for n in range(0, num+1):
    print(" " * n, end="")
    print("*" * (num - n))