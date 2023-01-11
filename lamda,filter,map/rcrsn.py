def getSum(num):
    if num == 1:
        return 1
    else:
        return num + getSum(num-1)
num = 10
print(getSum(num))
