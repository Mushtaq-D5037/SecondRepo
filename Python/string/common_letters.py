# find the common letters in a string

def common_letters():
    str1 = input('enter first string:')
    str2 = input('enter second string:')

    # taking unique letters or removing duplicates in a string
    set1 = set(str1)
    set2 = set(str2)

    # using intersection of sets to get the common letters
    cl = set1 and set2
    print(cl)

common_letters()