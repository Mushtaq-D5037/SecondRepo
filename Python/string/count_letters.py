# count the letters in a string
# First approach

str1 = 'aaaabbbccd'
str2 = 'irani chai chai chai irani'
str3 = 'aa bb cc dd bb cc bb cc aa'
str4 = 'aa,bb,cc,dd,bb,cc,bb,cc,aa,dd'

# First approach
# use count method of string to count the elements in a string
# before that separate the string elements (note check whether string has spaces, comma etc.,)
# use __contains__ method of string to check the separator
def count_letters(): 

    str = input("enter string:")

    # splitting string elements to list if it is not having spaces
    # using list comprehension, can also use for loop
    if str.__contains__(' ') == False:
        str_list  = [ i for i in str]
    
    # if has spaces, using split function
    else:
        str_list = str.split(' ')

    # keeping only unique elements using set property
    str_set = set(str_list)

    # appending elements and counts into empty list
    alpha = []
    count = []

    for i in str_set:
        c = str.count(i)
        alpha.append(i)
        count.append(c)

    # zipping elements & its count and converting it to a dictionary
    d = dict(zip(alpha, count))

    # printing
    print(d)

count_letters()

