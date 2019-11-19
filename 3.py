import fileinput
global summa
summa = 0
def replace_in_file(file_path, search_text, new_text):

    with fileinput.input(file_path, inplace=True) as f:

        for line in f:
            num = line.count(search_text)
            summa += num
            new_line = line.replace(search_text, new_text)
            print(new_line, end ='')
print("Count", summa)


file_path = 'D:\\Backups\\New Text Document.txt'
replace_in_file(file_path, 'gh', '123')