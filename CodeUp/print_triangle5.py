num = int(input())

for n in range(1, num+1, 2):
    print(" " * int((num-n)/2) + "*" * n) 