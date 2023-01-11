import os.path

file_path = r'C:\Users\Muhammed Jaseem\PycharmProjects\pythonProject\OOP\filehandling\sampleb5.txt'

sz = os.path.getsize(file_path)
print(f'The {file_path} size is',sz , 'bytes')
