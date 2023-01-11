import os

with open(r'C:\Users\Muhammed Jaseem\PycharmProjects\pythonProject\OOP\filehandling\sampleb5.txt')as fp:
    line_numbers = [0]
    lines=[]
    for i, line in enumerate(fp):
        if i in line_numbers:
            lines.append(line.strip())
print(lines)

