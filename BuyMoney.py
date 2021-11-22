# Task 2
s = int(input())
i = 0
arr = [500, 100, 10, 5, 2, 1]
posab = [0] * 5

while s > 0:
    if s - arr[i] < 0:
        i += 1    
    s -= arr[i]
    posab[i] += 1

for i in range(5):
    print(str(arr[i]) + ": " + str(posab[i]))

