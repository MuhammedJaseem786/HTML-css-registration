#To count number of lines
with open(r'C:\Users\Muhammed Jaseem\PycharmProjects\pythonProject\OOP\filehandling\sampleb5.txt')as fp:
    for count, lines in enumerate(fp):
        pass
print("number of line: ", count+1)