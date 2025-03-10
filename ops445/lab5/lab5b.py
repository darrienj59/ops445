#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file:
        
        return file.read()
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    with open(file_name) as file:
        file_list = file.readlines()
    for i in range(len(file_list)):
        file_list[i] = file_list[i].strip()
    return file_list
def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as file:
        file.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    file = open(file_name_read)
    lines = file.readlines()
    file.close()

    with open(file_name_write, 'w') as file:
        for i in range(len(lines)):
            file.write(f'{i + 1}:{lines[i]}')









if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First line\nSecond line\nThird Line\n'
    list1 = ['Line1', 'Line2', 'Line3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
    
