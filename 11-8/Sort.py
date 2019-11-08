list_numbers=[1,3,4,2]
list_sorted=[]


for number in range(0, len(list_numbers)):
    max = -5000
    for number in list_numbers:
        if number >= max:
            max = number
    list_numbers.remove(max)
    list_sorted.append(max)
print(list_sorted)
