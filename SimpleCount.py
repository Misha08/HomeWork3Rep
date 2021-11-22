count = int(input())
k = 0
for i in range(1, count):
    
    if k == 2:
        print(1)
        break
    
    if count % i == 0:
        k += 1

else:
    print(0)