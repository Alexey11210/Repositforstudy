import os
import time

print(os.getcwd())
os.chdir((r'D:\My Python Projects\Projects\Test_papka'))
print(os.getcwd())
for i in os.walk('.'):
    print(i)
directory = r'D:\My Python Projects\Projects\Test_papka'
filename = 'Test_File.txt'
root = os.path.join(directory, filename)
print(root)
mtime = os.path.getmtime(filename)
print(mtime)
filetime = time.ctime()
print(filetime)
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for  d in os.listdir() if os.path.isdir(d)]
print(file)
print(dirs)
fsize = os.path.getsize('Test_File.txt')
print(fsize)
directory_name = os.path.dirname(r'D:\My Python Projects\Projects\Test_File.txt')
print(directory_name)

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = directory
    filetime = filetime
    filesize = fsize
    parent_dir = directory_name
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}, Родительская директория: {parent_dir}')