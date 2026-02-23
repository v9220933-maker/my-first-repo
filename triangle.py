import time
size=10
for i in range(size):
    for j in range(size-i-1):
        print(" ",end="")
    for z in range(2*i+1):
        print("*",end="")
        time.sleep(0.1)
    print()