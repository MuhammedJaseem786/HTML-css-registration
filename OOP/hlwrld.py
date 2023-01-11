a = "hello world 123"
count1 = 0
count2 = 0
for i in a:
    if i.isalpha():
        count1 = count1 + 1
    elif i.isdigit():
        count2 = count2 +1
    elif i ==" ":
        i.rstrip()

print("letters: ", count1)
print("digits :", count2)




