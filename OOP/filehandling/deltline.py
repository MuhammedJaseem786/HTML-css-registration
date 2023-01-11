with open(r"C:\Users\Muhammed Jaseem\PycharmProjects\pythonProject\OOP\filehandling\sampleb5.txt", 'r') as fp:
    lines = fp.readlines()

with open(r"C:\Users\Muhammed Jaseem\PycharmProjects\pythonProject\OOP\filehandling\sampleb5.txt", 'w') as fp:
    for number, line in enumerate(lines):
        if number not in [0]:
          fp.write(line)