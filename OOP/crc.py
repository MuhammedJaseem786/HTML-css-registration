lst = []
for i in  range(1000,3001):
    if i % 2 == 0:
        lst.append(str(i))
print(','.join(lst))