str = 'aaaabccdeef'
str_list = [i for i in str]

d = {}
for i in str_list:
    if i not in d.keys():
        d[i]=0
    d[i]+=1

print(d)

counter=0
for idx in range(len(str)):
    if d[str[idx]]==1:
        print(str[idx], counter)
    else:
        counter+=1

