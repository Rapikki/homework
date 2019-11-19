print("Input path and file name:")
file_name = input()
print("Input line")
template = input()
#file_name = r"D:\\Backups\\New Text Document.txt"
file = open(file_name)
a = 0
b = 0
for line in file:
   # line = file.readline()
    #if (line == template):
    b = line.count(template)
    a +=b
print("Count",a)