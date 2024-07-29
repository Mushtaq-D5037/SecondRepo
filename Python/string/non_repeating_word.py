str = 'aaaabccdeef'
str_list = [i for i in str]

d = {}
for i in str_list:
    if i not in d.keys():
        d[i]=0
    d[i]+=1

print(d)
non_repeating_letters = []
for k, v in d.items():
    if v == 1:
        non_repeating_letters.append(k)

print(non_repeating_letters)


def non_repeating_words():

    str = input("enter string:")

    if str.__contains__(' ')==False:
        str_list = [ i for i in str]
    else:
        str_list = str.split()

    d = {}
    for i in str_list:
        if i not in d.keys():
            d[i]=0
        d[i]+=1

    non_repeating_letters = []
    for k, v in d.items():
        if v==1:
            non_repeating_letters.append(k)

    print(non_repeating_letters)

non_repeating_words()