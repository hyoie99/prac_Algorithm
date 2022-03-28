num = int(input())

for n in range(1, num+1):
    if(n==1 or n==num):
        print("*" * num)
    else:
        print("*" + " " * (num-2) + "*")