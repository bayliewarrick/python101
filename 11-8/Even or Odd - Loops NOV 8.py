activity = [1,2,4,6,23,4,5,435,62,691,583,596,34,95,37,26]

for x in range(len(activity) - 1,-1,-1):
    if(activity[x] % 2 == 0):
        print(f"{activity[x]} is even!")
    else:
        print(f"{activity[x]} is odd!")