#program will print all results in a given list less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for n in range(0,len(a)):
    if a[n] < 5:
        print(a[n])
    else:
        continue