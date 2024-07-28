# From a list of numbers, move 0 to the end of the list
my_list = [1, 2, 3, 0, 0, 4, 5, 6]

for item in my_list:
    if item==0:
        list.remove(item)
        list.append(item)

print(my_list)